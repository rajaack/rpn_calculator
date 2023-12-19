from Infrastructure.database import engine
from Infrastructure.models import Calculation
from sqlmodel import Session


def get_calculations_db(skip: int = 0, limit: int = 100):
    with Session(engine) as session:
        calculations = session.query(Calculation).offset(skip).limit(limit).all()
        return calculations


def get_calculation_db(calculation_id: int):
    with Session(engine) as session:
        return session.get(Calculation, calculation_id)
