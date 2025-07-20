# cleancode/__init__.py
# cleancode/sum_two_numbers.py
from typing import Union
class SumTwoNumbers:
    def __init__(self):
        pass
    def sum(self, num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        try:
            return num1 + num2
        except TypeError:
            raise ValueError("Input must be integers or floats")
def main() -> None:
    if __name__ == "__main__":
        s = SumTwoNumbers()
        result = s.sum(5.0, 3.0)
        print(f"The sum is: {result}")
if __name__ == "__main__":
    main()