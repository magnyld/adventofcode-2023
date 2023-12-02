import os.path

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''

def parse_input(s):
    return [
        [
            int(x.split(":")[0].split(" ")[1]), 
            ([([[int(s.split(" ")[0]) ,s.split(" ")[1]] for s in g.split(", ")]) for g in x.split(":")[1].strip().split("; ")])
        ] for x in s.strip().split("\n")
    ]

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)

    sum = 0
    for game in data:
        possible = True;
        for bags in game[1]:
            for set in bags:
                if(set[1] == "red" and set[0] > 12):
                    possible = False;
                
                if(set[1] == "green" and set[0] > 13):
                    possible = False;
                
                if(set[1] == "blue" and set[0] > 14):
                    possible = False;
                
        if (possible):
            sum += game[0];

    print(sum)

    return 0

if __name__ == "__main__":
    main()