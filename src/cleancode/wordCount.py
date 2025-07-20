# cleancode/word_counter.py
import re
class WordCounter:
    """Counts words in a given text."""
    def __init__(self, text: str):
        self.text = text
    def count_words(self) -> int:
        """Counts the number of words in the provided text."""
        return len(re.split(r'\W+', self.text))
def main() -> None:
    if __name__ == "__main__":
        try:
            text = input("Enter some text: ")
            counter = WordCounter(text)
            print(f"There are {counter.count_words()} words.")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
if __name__ == "__main__":
    main()