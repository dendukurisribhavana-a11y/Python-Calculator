def calculate(num1, operator, num2):

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2

    elif operator == "%":
        return num1 % num2

    else:
        return "Invalid operator"


def main():

    print("================================")
    print("       PYTHON CALCULATOR")
    print("================================")

    while True:

        print("\n1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "6":
            print("Thank you for using Calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            operators = {
                "1": "+",
                "2": "-",
                "3": "*",
                "4": "/",
                "5": "%"
            }

            operator = operators[choice]

            result = calculate(num1, operator, num2)

            print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")


if __name__ == "__main__":
    main()
