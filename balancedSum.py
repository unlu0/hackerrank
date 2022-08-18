#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    leftSum = 0
    rightSum = 0
    rightSum = sum(arr[1:])
    if rightSum == leftSum:
        return "YES"

    for i in range(1,len(arr)):
        leftSum += arr[i-1]
        rightSum -= arr[i]
        if leftSum == rightSum:
            return "YES"
    
    return "NO"

if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5, 6, 7]
    result = balancedSums(arr)
    print(result)