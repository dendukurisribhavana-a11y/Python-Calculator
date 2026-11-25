from calculator import calculate

print("Welcome to Python Calculator")

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Thank you for using Calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operators = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/"
        }

        result = calculate(num1, operators[choice], num2)
        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers!")
