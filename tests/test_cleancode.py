import pytest
from src.cleancode.word_counter import WordCounter

@pytest.mark.parametrize("text, expected_count", [
    ("Hello World!", 2),
    ("This is a test sentence.", 5),
    ("", 0),
    ("   ", 0),
    ("foo bar baz qux", 4)
])
def test_count_words(text: str, expected_count: int) -> None:
    sut = WordCounter(text)
    assert sut.count_words() == expected_count

@pytest.mark.parametrize("text, error_message", [
    ("hello world!", "Error occurred: no input"),
    ("", "Error occurred: no input")
])
def test_main_with_no_input(text: str, error_message: str) -> None:
    with pytest.raises(ValueError) as e_info:
        main()
    assert str(e_info.value) == error_message

def test_main_with_invalid_input() -> None:
    with pytest.raises(ValueError) as e_info:
        main()
    assert str(e_info.value) == "Error occurred: no input"

@pytest.mark.parametrize("text", [
    "hello world!",
    "This is a test sentence.",
    "foo bar baz qux"
])
def test_main_with_valid_input(text: str) -> None:
    with pytest.raises(SystemExit) as e_info:
        main()
    assert e_info.type == SystemExit
    out, err = capfd.readouterr()
    assert f"There are {WordCounter(text).count_words()} words." in out