#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    k %= 9
    n = n * k
    if len(n) == 1:
        return int(n)
    sumOfNumber = 0
    for i in n:
        sumOfNumber += int(i)
    return superDigit(str(sumOfNumber),1)

if __name__ == '__main__':

    result = superDigit("9875", 3)
    print(result)