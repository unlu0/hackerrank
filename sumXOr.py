#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(x):

    if x == 1 or x == 0:
        return 1

    y = math.floor(math.log2(x))
    if x - (2**y) == 0:
        return x

    if x > 2 ** y and x < 2 ** y + (2 ** y /2):
        return int(2 * sumXor(x + (2 ** y / 2)))
    else:
        return int(sumXor(x - (2 ** y)))

if __name__ == '__main__':

    print(sumXor(1000000000000000))
#1 2 3 4 5 6 7 8 9  
#  8 4 4 2 4 2 2 1
#16