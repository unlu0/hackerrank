#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])

    result = "YES"
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if i+1 < len(grid) and grid[i][j] > grid[i+1][j]:
                result = "NO"
                break

    return result

if __name__ == '__main__':
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']

        result = gridChallenge(grid)

        print(result)