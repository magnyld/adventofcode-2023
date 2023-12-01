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

def replaceStringWithNumber(s: str, x: str) -> str:
    if (x == "one"):
        s = s.replace(x, "1")

    if (x == "two"):
        s = s.replace(x, "2")

    if (x == "three"):
        s = s.replace(x, "3")

    if (x == "four"):
        s = s.replace(x, "4")

    if (x == "five"):
        s = s.replace(x, "5")

    if (x == "six"):
        s = s.replace(x, "6")

    if (x == "seven"):
        s = s.replace(x, "7")

    if (x == "eight"):
        s = s.replace(x, "8")

    if (x == "nine"):
        s = s.replace(x, "9")

    return s


def replaceFirstAndLast(s: str) -> str:

    r = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine))", s); # overlapping / look ahead
    
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