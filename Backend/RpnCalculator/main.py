import io
from datetime import datetime
from typing import Annotated

from Adapters.calculation_to_df import calculation_to_df
from Domain.rpn_calculator import rpn_calculator
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path
from fastapi.responses import StreamingResponse
from Infrastructure.database import create_db_and_tables
from Infrastructure.models import Calculation
from Selectors.calculation_selectors import get_calculation_db
from Selectors.calculation_selectors import get_calculations_db
from Services.calculation_services import create_calculation_db

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/get_csv")
async def get_csv(skip: int = 0, limit: int = 100):
    """

    Get a list of Calculations in csv file.

    Args:

        skip (int, optional): The number of items to skip. Defaults to 0.

        limit (int, optional): The maximum number of items to return. Defaults to 100.

    Returns:

        csv (StreamingResponse): A StreamingResponse containing a CSV file.

    """

    calculations = get_calculations_db(skip=skip, limit=limit)
    df = calculation_to_df(calculations)
    stream = io.StringIO()
    df.to_csv(stream, sep="|")
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response


@app.get("/calculations", response_model=list[Calculation])
async def read_calculations(skip: int = 0, limit: int = 100):
    """
    Get a list of Calculations.

    Args:

        skip (int, optional): The number of items to skip. Defaults to 0.

        limit (int, optional): The maximum number of items to return. Defaults to 100.

    Returns:

        list[Calculation]: A list of Calculations.
    """
    return get_calculations_db(skip=skip, limit=limit)


@app.get("/calculations/{calculation_id}", response_model=Calculation)
async def read_calculation(
    calculation_id: Annotated[int, Path(title="The ID of the item to get", ge=1)]
):
    """
    Get a single Calculation.

    Args:

        calculation_id (int, optional): The ID of the item to get. Defaults to 1.

    Returns:

        Calculation: A Calculation.
    """
    calculation = get_calculation_db(calculation_id=calculation_id)
    if not calculation:
        raise HTTPException(status_code=404, detail="Ressource non trouvée.")
    return calculation


@app.post("/calculations/", response_model=Calculation)
def create_calculation(operation: str):
    """
    Create a new Calculation.

    Args:

        operation (str): The operation in rpn calculator, example : 1 1 + 2 * will return result = 4

    Returns:

        Calculation: A Calculation.
    """

    try:
        result = rpn_calculator(operation.split(" "))
        calculation_db = Calculation(
            equation=operation, result=result, datetime=datetime.now()
        )
        calculation_db = create_calculation_db(calculation_db)
        return calculation_db

    except ValueError:
        raise HTTPException(
            status_code=400, detail="La syntaxe de la requête est erronée"
        )
    except ZeroDivisionError:
        raise HTTPException(
            status_code=400, detail="La division par zéro est impossible"
        )
