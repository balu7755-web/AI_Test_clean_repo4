import pytest
from my_package.main import Calculator

class TestCalculator:
    @pytest.fixture()
    def sut(self):
        return Calculator()

    def test_add(self, sut):
        assert math.isclose(sut.add(2.0, 3.0), 5.0)
        assert math.isclose(sut.add(-2.0, 3.0), 1.0)
        with pytest.raises(ValueError):
            sut.add('a', 3.0)

    def test_subtract(self, sut):
        assert math.isclose(sut.subtract(2.0, 3.0), -1.0)
        assert math.isclose(sut.subtract(-2.0, 3.0), -5.0)
        with pytest.raises(ValueError):
            sut.subtract('a', 3.0)

    def test_multiply(self, sut):
        assert math.isclose(sut.multiply(2.0, 3.0), 6.0)
        assert math.isclose(sut.multiply(-2.0, 3.0), -6.0)
        with pytest.raises(ValueError):
            sut.multiply('a', 3.0)

    def test_divide(self, sut):
        assert math.isclose(sut.divide(4.0, 2.0), 2.0)
        assert math.isclose(sut.divide(-4.0, 2.0), -2.0)
        with pytest.raises(ZeroDivisionError):
            sut.divide(4.0, 0.0)
        with pytest.raises(ValueError):
            sut.divide('a', 3.0)

def test_main():
    # main function is not tested here as it's an interactive shell
    pass