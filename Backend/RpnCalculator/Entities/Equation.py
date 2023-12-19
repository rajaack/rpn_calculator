from pydantic import BaseModel


class Equation(BaseModel):
    id: int
    equation: str

    def tolist(self):
        return self.equation.split(" ")
