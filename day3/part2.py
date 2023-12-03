import os.path

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

import re
pattern = re.compile(r"([0-9]|\.)")

#print(re.findall(pattern, "*"))

def parse_input(s):
    return [(list(filter(None, p))) for p in (re.split(r'(\d+|[^.])', x) for x in s.strip().split("\n"))]


def isNumber(s):
    return len(re.findall(r"[0-9]", s)) > 0

def checkAboveBelow(irow, charIndex, data, dir):
    ret = {"hits": 0, "sum": 1};

    wordPos = 0;
    for iword, word in enumerate(data[irow + dir]):

        if (not isNumber(word)):
            wordPos += len(word);
            continue;   

        lowBound = wordPos - 1;
        highBound = wordPos + 1 + len(word);
        if (lowBound <= charIndex and charIndex < highBound):
            #print("hit", word);
            ret["sum"] *= int(word);
            ret["hits"] += 1;

        #print(word);
        #print("lowBound:", lowBound);
        #print("highBound:", highBound);
        #print("wordPos:", wordPos);
        #print("charIndex:", charIndex);
        

        wordPos += len(word);

    return ret;


def checkBeforeAfter(irow, ipart, data):

    ret = {"hits": 0, "sum": 1};

    if(isNumber(data[irow][ipart-1])): 
        #print("hit", data[irow][ipart-1]);
        ret["sum"] *= int(data[irow][ipart-1]);
        ret["hits"] += 1;
    
    
    if (len(data[irow]) > ipart+1):
        if(isNumber(data[irow][ipart+1])):
            #print("hit", data[irow][ipart+1]);
            ret["sum"] *= int(data[irow][ipart+1]);
            ret["hits"] += 1;
    
    return ret;


def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)

    sum = 0
    for irow, row in enumerate(data):
        #print (row)

        for ipart, part in enumerate(row):
            if (len(re.findall(pattern, part)) == 0): #all symbols
                
                if(part == "*"): 
                    charIndex = len("".join(row[0:ipart]));
                    ret1 = checkBeforeAfter(irow, ipart, data);
                    ret2 = checkAboveBelow(irow, charIndex, data, -1);
                    ret3 = checkAboveBelow(irow, charIndex, data, +1);

                    sumHits = ret1["hits"] + ret2["hits"] + ret3["hits"];
                    if(sumHits >= 2 ):
                        sum += ret1["sum"] * ret2["sum"] * ret3["sum"];
       

    print(sum)

    return 0

if __name__ == "__main__":
    main()