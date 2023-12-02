import os.path
import re

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

def parse_input(s):
    return s.strip().split("\n")


def calculate_calibration_sum_corrected(document):
    total = 0
    number_words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    for line in document:
        # Replace spelled-out numbers with digits
        for word, digit in number_words.items():
            line = line.replace(word, digit)

        first_digit = None
        last_digit = None

        # Find the first digit
        for char in line:
            if char.isdigit():
                first_digit = char
                break

        # Find the last digit
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break

        # Combine first and last digits to form a number, then add it to the total
        if first_digit is not None and last_digit is not None:
            calibration_value = int(first_digit + last_digit)
            total += calibration_value

    return total


def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_TEST_DATA)
    #data = parse_input(INPUT_DATA)

    # Calculate the sum for the provided document
    sum_of_calibration_values = calculate_calibration_sum_corrected(data)
    print(sum_of_calibration_values)

    return 0

if __name__ == "__main__":
    main()