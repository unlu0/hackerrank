#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    result = 0

    for i in range(len(s)):
        subList = []
        subListCheck = True
        for j in range(m):
            if i + j == len(s):
                subListCheck = False
                break
            subList.append(s[i+j])

        if subListCheck:
            if sum(subList) == d:
                result += 1

    return result

if __name__ == '__main__':

    result = birthday([1,2,1,3,2], 3, 2)
    print(result)
