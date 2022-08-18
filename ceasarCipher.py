#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
import re

def caesarCipher(s, k):
    result = ""
    k = k % 26

    for i in s:
        if re.match(r"[a-z]+",i):
            cipherInt = ord(i)+k
            if cipherInt > ord('z'):
                cipherInt -= 26
            i = chr(cipherInt)
        elif re.match(r"[A-Z]+",i):
            cipherInt = ord(i)+k
            if cipherInt > ord('Z'):
                cipherInt -= 26
            i = chr(cipherInt)
        
        result += i
        
    return result

if __name__ == '__main__':

    result = caesarCipher("middle-Outz", 2)
    print(result)

