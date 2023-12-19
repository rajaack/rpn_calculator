import pytest

from Backend.RpnCalculator.Entities.Equation import Equation
from Backend.RpnCalculator.Entities.rpn_calculator import rpn_calculator


class TestRPNCalculator:
    """Test Reverse Polish Notation Calculator"""

    def test_sum_between_two_numbers(self):
        equation = Equation(id=1, equation="1 2 +")
        assert rpn_calculator(equation) == 3

    def test_subtract_two_numbers(self):
        equation = Equation(id=1, equation="1 2 -")
        assert rpn_calculator(equation) == 1

    def test_multiplication_of_two_numbers(self):
        equation = Equation(id=1, equation="1 2 *")
        assert rpn_calculator(equation) == 2

    def test_division_of_two_numbers(self):
        equation = Equation(id=1, equation="2 1 /")
        assert rpn_calculator(equation) == 0.5

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            equation = Equation(id=1, equation="0 2 /")
            rpn_calculator(equation)

    def test_equation_with_two_operators(self):
        equation = Equation(id=1, equation="3 10 5 + * 5 + 10 *")
        assert rpn_calculator(equation) == 500

    def test_equation_with_error_in_equation(self):
        with pytest.raises(ValueError):
            equation = Equation(id=1, equation="1 1 a")
            rpn_calculator(equation)
