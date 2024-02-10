def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero."

def calculator():
    while True:
        print("Simple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 5:
                print("Exiting the calculator.")
                break

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        operations = {1: add, 2: subtract, 3: multiply, 4: divide}

        if choice in operations:
            result = operations[choice](num1, num2)
            print(f"Result: {num1} {'+-*/'[choice-1]} {num2} = {result}")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        ask_to_exit = input("Do you want to perform another operation? (yes/no): ").lower()
        if ask_to_exit != 'yes':
            print("Exiting the calculator.")
            break

if __name__ == "__main__":
    calculator()
