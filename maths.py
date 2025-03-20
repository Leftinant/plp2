def simple_calculator():
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return  # Exit the function
            result = num1 / num2
        else:
            print("Error: Invalid operation.")
            return  # Exit the function

        print("Result:", result)
# This is a simple calculator program that performs basic arithmetic operations.

    # Call the calculator function
if __name__ == "__main__":
    simple_calculator()