#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower()
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    counts = [0 for i in range(len(chars))]
    
    for i in s:
        if i in chars:
            counts[chars.index(i)] += 1

    for i in counts:
        if i == 0:
            return "not pangram"

    return "pangram"

if __name__ == '__main__':

    s = "We promptly judged antique ivory buckles for the next prize"

    result = pangrams(s)

    print(result)

