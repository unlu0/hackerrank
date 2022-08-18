#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sockDict = dict()
    for i in ar:
        if i not in sockDict.keys():
            sockDict[i] = 1
        else:
            sockDict[i] = sockDict[i] + 1

    pairCount = 0

    for i in sockDict.keys():
        pairCount += sockDict[i]//2

    return pairCount

if __name__ == '__main__':

    result = sockMerchant(3, [10,20,20,10,10,30,50,10,20])
    print(result)