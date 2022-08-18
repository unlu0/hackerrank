#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sumOfFirstDiagonal = 0
    sumOfSecondDiagonal = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                sumOfFirstDiagonal += arr[i][j]
            if abs(i+j) == len(arr) - 1:
                sumOfSecondDiagonal += arr[i][j]
    
    result = abs(sumOfFirstDiagonal - sumOfSecondDiagonal)
    return result


if __name__ == '__main__':


    arr = [[1,2,3],[4,5,6],[7,8,9]]
    arr = [[11,2,4],[4,5,6],[10,8,-12]]

    result = diagonalDifference(arr)
    print(result)


