import os.path

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

def parse_input(s):
    return [
        [
            x.split(":")[0].split(" ")[1], 
            
            list(int(n) for n in (list(filter(None, x.split(":")[1].split("|")[0].split(" "))))),
            list(int(n) for n in (list(filter(None, x.split(":")[1].split("|")[1].split(" ")))))
        
        ] for x in s.strip().split("\n")
    ]

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)

    newCards = [1] * len(data);

    for i, card in enumerate(data):
        for k in range(0, newCards[i]): # process each card multiple times
            match = 0;
            for winning in card[1]:
                for mynum in card[2]:
                    if (mynum == winning):
                        match = match + 1 

            for m in range(0, match):
                newCards[i+m+1] = newCards[i+m+1] + 1;

    print(sum(newCards));
    
    return 0

if __name__ == "__main__":
    main()