#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeCheck(s):
    start = 0
    end = len(s)-1
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True

def palindromeIndex(s):
    # Write your code here
    if palindromeCheck(s):
        return -1
    for i in range(len(s)):
        s1 = ""
        if i == 0:
            s1 = s[1:]
        elif i == len(s)-1:
            s1 = s[:-1]
        else:
            s1 = s[:i] + s[i+1:]
        if palindromeCheck(s1):
            return i
    return -1

if __name__ == '__main__':
    print(palindromeIndex("abc"))
    print(palindromeIndex("aba"))
    print(palindromeIndex("cbadbc"))
    print(palindromeIndex("baa"))
    print(palindromeIndex("aaa"))