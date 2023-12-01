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

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

def replaceStringWithNumber(s: str, sNumber: str) -> str:

    for i, number in enumerate(numbers):
        if(sNumber == number):
            s = s.replace(sNumber, str(i+1))

    return s

def replaceFirstAndLast(s: str) -> str:

    r = re.findall("(?=(" + "|".join(numbers) + "))", s); # overlapping / look ahead
    
    if(len(r) > 0):
        return replaceStringWithNumber(s, r[0]) + replaceStringWithNumber(s, r[len(r)-1])

    return s


def parse_input(s: str) -> list[int]:
    return [
        re.sub(r'[^0-9]', '',
            replaceFirstAndLast(x)
        )
        for x in s.strip().split("\n")
    ]

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)
    sum = 0
    for row in data:
        sum += int(row[0] + row[len(row) -1])

    print(sum)

    return 0

if __name__ == "__main__":
    main()