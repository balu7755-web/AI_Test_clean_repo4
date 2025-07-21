# cleancode/calculator.py
from typing import Union
class Calculator:
    def __init__(self):
        pass
    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        try:
            return a + b
        except TypeError:
            raise ValueError("Both inputs must be numbers")
    def subtract(self, a: float, b: float) -> float:
        """Subtract one number from another."""
        try:
            return a - b
        except TypeError:
            raise ValueError("Both inputs must be numbers")
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        try:
            return a * b
        except TypeError:
            raise ValueError("Both inputs must be numbers")
    def divide(self, a: float, b: float) -> Union[float, ValueError]:
        """Divide one number by another."""
        try:
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        except TypeError:
            raise ValueError("Both inputs must be numbers")
def main():
    calc = Calculator()
    print("Simple Calculator")
    while True:
        user_input = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        try:
            num1, operator, num2 = map(str.strip, user_input.split())
            num1, num2 = float(num1), float(num2)
            if operator == '+':
                print(calc.add(num1, num2))
            elif operator == '-':
                print(calc.subtract(num1, num2))
            elif operator == '*':
                print(calc.multiply(num1, num2))
            elif operator == '/':
                try:
                    print(calc.divide(num1, num2))
                except ValueError as e:
                    print(str(e))
        except ValueError as e:
            print(str(e))
if __name__ == "__main__":
    main()