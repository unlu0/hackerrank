#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    turn = ["Richard","Louise"]
    count = 0
    while n != 1:
        count+=1
        log = math.log2(n)
        if  log - log//1 == 0:
            n /= 2
        else:
            n -= 2**(log//1)

    return turn[count%2]



if __name__ == '__main__':

    result = counterGame(1560834904)
    print(result)
    result = counterGame(1768820483)
    print(result)
    result = counterGame(1533726144)
    print(result)
    result = counterGame(1620434450)
    print(result)
    result = counterGame(1463674015)
    print(result)

