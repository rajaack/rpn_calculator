from Backend.Common.measure_time_func_decorator import measure_time_func
from Backend.RpnCalculator.Entities.Equation import Equation

OPERATORS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


@measure_time_func
def rpn_calculator(equation: Equation) -> float:
    """
    Reverse Polish Notation Calculator
    https://en.wikipedia.org/wiki/Reverse_Polish_notation

    Args:
        equation: the equation to be evaluated contains operators and integers

    Returns: last value of the stack

    """

    stack = []
    for input in equation.tolist():
        if input.isdigit():
            stack.append(float(input))
        elif input in OPERATORS.keys():
            value = OPERATORS[input](stack.pop(), stack.pop())
            stack.append(value)
        else:
            raise ValueError(f"Invalid input: {input}")

    return stack.pop()
