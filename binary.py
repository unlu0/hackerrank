#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binary = str(bin(n))
    binary = binary[2:]
    print(binary)
    while len(binary) < 32:
        binary = "0" + binary
    print(binary)
    binaryInverse = 0
    for i in range(len(binary)-1,-1,-1):
        if binary[i] == "0":
            binaryInverse += 2 ** (31-i)

    print(binaryInverse)    

if __name__ == '__main__':

    n = 9

    result = flippingBits(n)

