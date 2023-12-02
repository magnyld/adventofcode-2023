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
    return [re.sub(r'[^0-9]', '', x) for x in s.strip().split("\n")]

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