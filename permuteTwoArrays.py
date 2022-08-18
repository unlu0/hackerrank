#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def findNearestMinIndex(k, a, B):
    dif = sys.maxsize
    nearestIndex = -1
    for i in range(len(B)):
        if a + B[i] == k:
            return i
        if (a + B[i] - k) >= 0 and  (a + B[i] - k) < dif:
            dif = a + B[i] - k
            nearestIndex = i

    return nearestIndex

def twoArrays(k, A, B):
    # Write your code here
    BNew = list()
    for a in A:
        nearestMinIndex = findNearestMinIndex(k,a,B)
        if nearestMinIndex == -1:
            return "NO"
        BNew.append(B[nearestMinIndex])
        del B[nearestMinIndex]

    print(A)
    print(BNew)

    for a,b in zip(A,BNew):
        if a + b < k:
            return "NO"

    return "YES"

if __name__ == '__main__':
    list1 = list(map(int, "3 6 8 5 9 9 4 8 4 7".split()))
    list2 = list(map(int, "5 1 0 1 6 4 1 7 4 3".split()))
    k = 9
    result = twoArrays(k, list1, list2)
    print(result)
"""     result = twoArrays(5, [2,3,1,1,1], [1,3,4,3,3])
    print(result) """

