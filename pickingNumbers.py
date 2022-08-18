#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    setA = set(a)
    countMax = 0
    for i in setA:
        count1 = 0
        count2 = 0
        index = a.index(i)
        for j in range(index,len(a)):
            if a[j] == i or a[j] == i+1:
                count1 += 1
            if a[j] == i or a[j] == i-1:
                count2 += 1
        if count1 > count2 and count1 > countMax:
            countMax = count1
        elif count2 >= count1 and count2 > countMax:
            countMax = count2
        
    return countMax  
        

if __name__ == '__main__':
    
    a = list(map(int, "1 2 2 3 1 2".split()))

    result = pickingNumbers(a)

    print(result)