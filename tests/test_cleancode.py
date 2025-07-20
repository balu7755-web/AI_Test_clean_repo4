

import pytest
from src.cleancode.main import SumNumbers, add, validate_input, main


def test_add():
    sut = SumNumbers()
    assert add(1.0, 2.0) == 3.0
    assert add(-1.0, -2.0) == -3.0
    assert add(float('nan'), float('inf')) == float('nan')
    with pytest.raises(TypeError):
        add('a', 2)
    with pytest.raises(TypeError):
        add(1, 'b')


def test_validate_input():
    sut = SumNumbers()
    assert validate_input('1.0', '2.0') == (1.0, 2.0)
    assert validate_input('-1.0', '-2.0') == (-1.0, -2.0)
    with pytest.raises(ValueError):
        sut.validate_input('a', 'b')
    with pytest.raises(ValueError):
        sut.validate_input('1.0', 'abc')


def test_main():
    with pytest.raises(SystemExit) as e:
        main()
    assert e.type == SystemExit
    expected_output = "Error: invalid input\n"
    with open("test.txt", "w") as f:
        f.write(expected_output)
    try:
        main()
        assert False, "Expected an error"
    except SystemExit:
        pass

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        ("1.0", "2.0", (1.0, 2.0)),
        ("-1.0", "-2.0", (-1.0, -2.0)),
        ("a", "b", None),
    ]
)
def test_validate_input_parametrize(num1, num2, expected):
    sut = SumNumbers()
    result = sut.validate_input(num1, num2)
    assert result == expected