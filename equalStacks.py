#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
def decreaseHeight(minSum,h1,h2,sumH1,sumH2):
    while sumH1 > minSum:
         sumH1 -= h1[0]
         del h1[0]
    
    while sumH2 > minSum:
         sumH2 -= h2[0]
         del h2[0]
         
    return sumH1,sumH2
    
def equalStacks(h1, h2, h3):
    # Write your code here
    sumH1 = sum(h1)
    sumH2 = sum(h2)
    sumH3 = sum(h3)
    minSum = sys.maxsize
    
    while minSum > 0:
        minSum = min([sumH1,sumH2,sumH3])
        
        if minSum == sumH1:
            sumH2,sumH3 = decreaseHeight(minSum,h2,h3,sumH2,sumH3)
            if sumH2 == minSum and sumH3 == minSum:
                return minSum
            else:
                sumH1 -= h1[0]
                del h1[0]
        elif minSum == sumH2:
            sumH1,sumH3 = decreaseHeight(minSum,h1,h3,sumH1,sumH3)
            if sumH1 == minSum and sumH3 == minSum:
                return minSum
            else:
                sumH2 -= h2[0]
                del h2[0]
        elif minSum == sumH3:
            sumH1,sumH2 = decreaseHeight(minSum,h1,h2,sumH1,sumH2)
            if sumH1 == minSum and sumH2 == minSum:
                return minSum
            else:
                sumH3 -= h3[0]
                del h3[0]
    
    return -1
    
if __name__ == '__main__':
    result = equalStacks([3,2,1,1,1], [4,3,2], [1,1,4,1])
    print(result)

