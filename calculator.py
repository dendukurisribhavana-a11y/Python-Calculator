def calculate(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2

    elif operator == "%":
        if num2 == 0:
            raise ZeroDivisionError("Cannot calculate modulus by zero")
        return num1 % num2

    else:
        raise ValueError("Invalid operator")
