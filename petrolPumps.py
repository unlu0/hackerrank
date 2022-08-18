#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#  

def truckTour(petrolpumps):
    # Write your code here
    for i in range(len(petrolpumps)):
        petrol = 0
        t = i
        count = 0
        while count < len(petrolpumps):
            petrol += petrolpumps[t][0]
            petrol -= petrolpumps[t][1]
            if petrol < 0:
                break
            t += 1
            if t == len(petrolpumps):
                t = 0
            if t == i:
                return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
