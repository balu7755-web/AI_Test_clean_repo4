Here is a professional README.md for the Python project 'cleancode':

📖 Overview
================

Cleancode is a simple Python program designed to count the number of words in a given text file. This project aims to provide a straightforward and efficient solution for counting word frequencies.

⚙️ Installation Instructions
==========================

1. Clone this repository using `git clone https://github.com/your-username/cleancode.git`
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Run the program using `python cleancode.py` (assuming you have Python installed)

🚀 Usage Examples
================

### Counting word frequencies in a file:

1. Save your text file with words you want to count.
2. Run the program: `python cleancode.py <your-file-name.txt>`
3. The output will display the word frequency for each unique word.

### Specifying a custom threshold:

1. Pass a threshold value as an argument: `python cleancode.py <your-file-name.txt> 5`
2. The program will only count words that appear at least 5 times in the file.

✅ Testing Information
=====================

To run tests, use the following command:
```
pytest tests/test_cleancode.py
```
This will execute all test cases and provide a summary of the results.

📜 License
==========

Cleancode is licensed under the MIT License. See [LICENSE](LICENSE) for details.