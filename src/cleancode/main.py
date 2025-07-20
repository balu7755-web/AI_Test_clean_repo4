# cleancode/sum.py
from typing import Union
class Calculator:
    """Simple calculator for sum operations."""
    def add(self, a: float, b: float) -> Union[float, str]:
        """Add two numbers and return the result as a string or an error message."""
        try:
            return f"The sum is {a + b}."
        except TypeError:
            return "Error: Both inputs must be numbers."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
def main() -> None:
    """Entry point for standalone execution."""
    calc = Calculator()
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(calc.add(num1, num2))
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()