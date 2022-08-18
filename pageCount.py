#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if n % 2 == 0:
        n = n + 1
    
    x = p // 2
    y = (n - p) //2
    
    if x < y:
        return x
    else:
        return y

if __name__ == '__main__':

    result = pageCount(6, 5)
    print(result)

