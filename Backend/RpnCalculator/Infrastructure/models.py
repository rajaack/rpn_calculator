from datetime import datetime
from typing import Optional

from sqlmodel import Field
from sqlmodel import SQLModel


class Calculation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    equation: str
    result: float
    datetime: datetime
