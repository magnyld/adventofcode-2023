import os.path
import re

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''

def parse_input(s):
    return s.strip().split("\n")


def calculate_calibration_sum(document):
    total = 0
    for line in document:
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

# The document you provided
provided_document = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)

    # Calculate the sum for the provided document
    sum_of_calibration_values = calculate_calibration_sum(data)
    print(sum_of_calibration_values)

    return 0

if __name__ == "__main__":
    main()