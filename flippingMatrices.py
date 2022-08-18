#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def exchange(matrix, r, i, r1, j):
    hold = matrix[r][i]
    matrix[r][i] = matrix[r1][j]
    matrix[r1][j] = hold

def flipRow(matrix,r):
    j = len(matrix[r])-1
    i = 0
    while i <= j:
        exchange(matrix,r,i,r,j)
        i += 1
        j -= 1

def flipColumn(matrix,c):
    j = len(matrix[0])-1
    i = 0
    while i <= j:
        exchange(matrix,j,c,i,c)
        i += 1
        j -= 1

def findMaxIndex(matrix):
    maxNumber = 0
    maxColIndex = -1
    maxRowIndex = -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > maxNumber:
                maxNumber = matrix[i][j]
                maxRowIndex = i
                maxColIndex = j

    return maxRowIndex,maxColIndex

def flippingMatrix(matrix):
    # Write your code here
    result = 0
    count = int(len(matrix) * len(matrix[0]) / 4)
    for i in range(count):
        i,j = findMaxIndex(matrix)
        result += matrix[i][j]
        matrix[i][j] = float("-inf")

    return result
        

matrix = [[1,2],[3,4]]


result = flippingMatrix(matrix)
print(result)
