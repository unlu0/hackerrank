#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    l = list()
    bracketDict = {"}":"{","]":"[",")":"("}
    
    for i in s:
        if i in ["{","[","("]:
            l.append(i)
        elif i in ["}","]",")"]:
            if len(l) == 0 or l.pop() != bracketDict[i]:
                return "NO"
    if len(l) > 0:
        return "NO"
    return "YES"    

if __name__ == '__main__':

    result = isBalanced("[{")
    print(result)
    result = isBalanced("{}([{()[]{{}}}])({})")
    print(result)
   