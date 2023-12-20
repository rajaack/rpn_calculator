from Infrastructure.database import engine
from Infrastructure.models import Calculation
from sqlmodel import Session


def create_calculation_db(calculation: Calculation):
    with Session(engine) as session:
        session.add(calculation)
        session.commit()
        session.refresh(calculation)
    return calculation
