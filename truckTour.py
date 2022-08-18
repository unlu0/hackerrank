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
    pumpDict = dict()
    for pump in petrolpumps:
        pumpDict[pump[0]] = pump[1]
    
    pumpDictKeys = sorted(pumpDict.keys())

    petrol = 0
    result = True
    for i in range(len(pumpDictKeys)):
        petrol += pumpDict[pumpDictKeys[i]]
        if i + 1 < len(pumpDictKeys):
            petrol -= abs(pumpDictKeys[i+1] - pumpDictKeys[i])
        if petrol < 0:
            result = False
            break

    if result:
        return pumpDictKeys[0]
    
    result = True
    pumpDictKeys.reverse()

    for i in range(len(pumpDictKeys)):
        petrol += pumpDict[pumpDictKeys[i]]
        if i + 1 < len(pumpDictKeys):
            petrol -= abs(pumpDictKeys[i+1] - pumpDictKeys[i])
        if petrol < 0:
            result = False
            break
    if result:
        return pumpDictKeys[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
