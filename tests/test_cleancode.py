import pytest

from src.cleancode.main import SumTwoNumbers, main


#from src.cleancode.sum_two_numbers import SumTwoNumbers

def test_sum_two_numbers():
    sut = SumTwoNumbers()
    assert sut.sum(2, 3) == 5
    assert sut.sum(-2, -3) == -5
    assert sut.sum(0.0, 0.0) == 0.0
    with pytest.raises(ValueError):
        sut.sum(1, 'a')
    with pytest.raises(ValueError):
        sut.sum('a', 1)

def test_sum_two_numbers_main():
    main()