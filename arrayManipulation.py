#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    l = [0 for i in range(n)]
    print(l)
    for query in queries:
        l[query[0]-1] += query[2]
        if query[1] < n:
            l[query[1]] -= query[2]
    
    maxSum = 0
    tempSum =0
            
    for i in l:
        tempSum += i
        if tempSum > maxSum:
            maxSum = tempSum
        
    return maxSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
