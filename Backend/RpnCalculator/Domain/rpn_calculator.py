OPERATORS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}


def rpn_calculator(equation: list) -> float:
    """
    Reverse Polish Notation Calculator
    https://en.wikipedia.org/wiki/Reverse_Polish_notation

    Args:
        equation: the equation to be evaluated contains operators and integers

    Returns: last value of the stack

    """

    stack = []
    for item in equation:
        if item.isdigit():
            stack.append(float(item))
        elif item in OPERATORS.keys() and len(stack) >= 2:
            value = OPERATORS[item](stack.pop(), stack.pop())
            stack.append(value)
        else:
            raise ValueError(f"Invalid input: {item}")

    return stack.pop()
