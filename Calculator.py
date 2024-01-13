class SimpleCalculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"

    def perform_calculation(self, operation, x, y):
        if operation == '1':
            return self.add(x, y), "Addition"
        elif operation == '2':
            return self.subtract(x, y), "Subtraction"
        elif operation == '3':
            return self.multiply(x, y), "Multiplication"
        elif operation == '4':
            return self.divide(x, y), "Division"
        else:
            return None, None

def main():
    calculator = SimpleCalculator()

    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    operation = input("Enter operation choice (1-4): ")

    if operation not in ('1', '2', '3', '4'):
        print("Invalid choice. Please enter a number between 1 and 4.")
        return

    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))

    result, operation_name = calculator.perform_calculation(operation, x, y)

    if result is not None:
        print(f"{operation_name} result: {result}")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
