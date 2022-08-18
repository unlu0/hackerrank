#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr = sorted(arr)
    index = 0
    dif = sys.maxsize

    for i in range(len(arr)):
        if k - 1 + i == len(arr):
            break
        
        if arr[k-1+i] - arr[i] < dif:
            index = i
            dif = arr[k-1+i] - arr[i]

    return arr[k-1 + index] - arr[index]


if __name__ == '__main__':

    result = maxMin(4, [1,2,3,4,10,20,30,40,100,200])
    print(result)
