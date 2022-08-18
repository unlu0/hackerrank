import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plusCount = 0
    minusCount = 0
    zeroCount = 0
    for i in arr:
        if i > 0:
            plusCount+=1
        elif i < 0:
            minusCount+=1
        else:
            zeroCount+=1

    print(plusCount/len(arr))
    print(minusCount/len(arr))
    print(zeroCount/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)