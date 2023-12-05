import os.path

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

def parse_input(s):
    return [
        list(int(s) for s in s.strip().split("\n\n")[0].split(":")[1].strip().split(" ")),
        list (list(list(int(v) for v in n.split(" ")) for n in m.split("\n")[1:]) for m in s.strip().split("\n\n")[1:]),
    ]

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    #data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)

    #print(data);
    #print(data[0]); #seeds
    
    ret = -1;

    for seed in data[0]:
        res = seed;
        #print(res);
        for i in range(0,7): # all 7 types
                    
            for lookup in data[1][i]:
                
                start = lookup[1];
                end = lookup[1] + lookup[2];
                
                if(res >= start and res < end):
                    oldres = res;
                    res = (res-start)+lookup[0];
                    #print("hit", start, end, res, oldres);
                    break;
            
            #print(i, res);

        if(ret == -1):
            ret = res;
        else:
            ret = min(ret, res);
        
    print(ret);
   
    return 0

if __name__ == "__main__":
    main()