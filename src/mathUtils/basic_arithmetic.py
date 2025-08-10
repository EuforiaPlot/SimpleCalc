def arithmetic_operator(a, b, operators):
    match operators:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                raise ZeroDivisionError("\nZero Divison Error.\n")
            return a / b
        case _:
            raise ValueError(f"\nOperator not recognized: {operators}\n")

