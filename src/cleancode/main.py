# cleancode/sum_numbers.py
import sys
class SumNumbers:
    def __init__(self):
        pass
    def add(self, a: float, b: float) -> float:
        """
        Returns the sum of two numbers.
        Args:
            a (float): The first number.
            b (float): The second number.
        Returns:
            float: The sum of a and b.
        """
        return a + b
    def validate_input(self, num1: str, num2: str) -> tuple:
        """
        Validates input numbers and returns them as floats or raises ValueError if invalid.
        Args:
            num1 (str): The first number.
            num2 (str): The second number.
        Returns:
            tuple: A tuple containing the validated numbers as floats.
        """
        try:
            return float(num1), float(num2)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    def main(self):
        if __name__ == "__main__":
            try:
                num1, num2 = self.validate_input(input("Enter the first number: "), input("Enter the second number: "))
                result = self.add(num1, num2)
                print(f"The sum of {num1} and {num2} is: {result}")
            except Exception as e:
                print(f"Error: {e}", file=sys.stderr)
                sys.exit(1)
if __name__ == "__main__":
    main()