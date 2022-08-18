#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#
def binarySearch(liste,searchedElement):
    maxl = len(liste)-1
    minl = 0
    while minl <= maxl :
        mid = (maxl + minl)//2 
        if liste[mid] == searchedElement :
            return mid
        elif liste[mid] < searchedElement :
            minl = mid + 1
        else:
            maxl = mid -1 

    return -1
    
def pairs(k, arr):
    # Write your code here
    count = 0
    arr = sorted(arr)
    for i in arr:
        if binarySearch(arr,i+k) != -1:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
