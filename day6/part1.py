import os.path
import math

INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')

INPUT_TEST_DATA = '''\
Time:      7  15   30
Distance:  9  40  200
'''

def parse_input(s):
    return [
        list(map(int, list(filter(None, x.split(" ")))[1:])) for x in s.strip().split("\n")
    ]

def beatTime(buttonTime, run, record):

    runlength = (run-buttonTime) * buttonTime;

    #print(buttonTime, run, record, runlength);
    
    if(runlength > record):
        return runlength
    else: 
        return 0

def main() -> int:

    f = open(INPUT_FILE)
    INPUT_DATA = f.read();

    data = parse_input(INPUT_TEST_DATA)
    data = parse_input(INPUT_DATA)
    
    sum = [];


    for i, run in enumerate(data[0]):
        record = data[1][i];
        #print("new run", run, record);

        runtotal = [];
        for n in range(1, run):
            runspeed = beatTime(n, run, record);
            if(runspeed != 0):
                runtotal.append(runspeed);
                #print("beat time", n, runspeed);

        sum.append(len(runtotal));

    print(math.prod(sum))

    return 0

if __name__ == "__main__":
    main()