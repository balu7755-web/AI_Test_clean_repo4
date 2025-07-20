# cleancode/sum.py
def __init__():
    pass
class Number:
    def __init__(self, value: int):
        self.value = value
    def get_value(self) -> int:
        """Get the number's value"""
        return self.value
    def __add__(self, other: 'Number') -> int:
        """Add this number with another number"""
        if not isinstance(other, Number):
            raise ValueError("Both inputs must be instances of Number")
        return self.value + other.get_value()
class SumCalculator:
    def __init__(self, num1: Number, num2: Number):
        self.num1 = num1
        self.num2 = num2
    def calculate_sum(self) -> int:
        """Calculate the sum of two numbers"""
        try:
            return self.num1 + self.num2
        except ValueError as e:
            print(f"Error: {str(e)}")
            return None
def main():
    num1 = Number(10)
    num2 = Number(20)
    calculator = SumCalculator(num1, num2)
    result = calculator.calculate_sum()
    if result is not None:
        print("The sum is:", result)
if __name__ == "__main__":
    main()