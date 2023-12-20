import pytest

from Backend.RpnCalculator.Domain.rpn_calculator import rpn_calculator


class TestRPNCalculator:
    """Test Reverse Polish Notation Calculator"""

    def test_sum_between_two_numbers(self):
        equation = "1 2 +"
        assert rpn_calculator(equation.split(" ")) == 3

    def test_subtract_two_numbers(self):
        equation = "1 2 -"
        assert rpn_calculator(equation.split(" ")) == 1

    def test_multiplication_of_two_numbers(self):
        equation = "1 2 *"
        assert rpn_calculator(equation.split(" ")) == 2

    def test_division_of_two_numbers(self):
        equation = "2 1 /"
        assert rpn_calculator(equation.split(" ")) == 0.5

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            equation = "0 2 /"
            rpn_calculator(equation.split(" "))

    def test_equation_with_two_operators(self):
        equation = "3 10 5 + * 5 + 10 *"
        assert rpn_calculator(equation.split(" ")) == 500

    def test_equation_with_error_in_equation(self):
        with pytest.raises(ValueError):
            equation = "1 1 a"
            rpn_calculator(equation.split(" "))

    def test_equation_error(self):
        with pytest.raises(ValueError):
            equation = "1 + -"
            rpn_calculator(equation.split(" "))
