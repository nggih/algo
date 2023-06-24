#!/bin/python3


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley = 0
    level = 0
    prev_d = 0
    seq = []
    for p in path:
        if p == "U": 
            level += 1
            prev_d = 0
            seq = []
        if p == "D": 
            prev_d += 1
            if len(seq) <= 1:
                seq.append("D") 
            level -= 1
            if len(seq) == 2 and level < 0 and prev_d == 2:
                valley += 1

        print(prev_d, level, seq, valley)

    return valley

steps = 8
path = "DUDDDUUDUU"
count = countingValleys(steps, path)
print(count == 2)
