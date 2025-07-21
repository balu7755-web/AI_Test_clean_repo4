import pytest
from my_package.main import Calculator

class TestCalculator:
    def test_add(self):
        calc = Calculator()
        assert math.isclose(calc.add(1.0, 2.0), 3.0)
        assert not math.isinf(calc.add(-1.0, 2.0))
        with pytest.raises(ValueError):
            calc.add('a', 'b')
    
    def test_subtract(self):
        calc = Calculator()
        assert math.isclose(calc.subtract(1.0, 2.0), -1.0)
        assert not math.isnan(calc.subtract(-1.0, 2.0))
        with pytest.raises(ValueError):
            calc.subtract('a', 'b')
    
    def test_multiply(self):
        calc = Calculator()
        assert math.isclose(calc.multiply(1.0, 2.0), 2.0)
        assert not math.isinf(calc.multiply(-1.0, 2.0))
        with pytest.raises(ValueError):
            calc.multiply('a', 'b')
    
    def test_divide(self):
        calc = Calculator()
        assert math.isclose(calc.divide(4.0, 2.0), 2.0)
        with pytest.raises(ZeroDivisionError):
            calc.divide(1.0, 0.0)
        with pytest.raises(ValueError):
            calc.divide('a', 'b')