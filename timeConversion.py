#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2:] == "PM":
        s=s[:-2]
        hour1 = int(s[0])
        hour2 = int(s[1])
        if hour1*10+hour2 < 12:
            hour = str(hour1*10+hour2+12)
        else:
            hour = str(hour1*10+hour2)
        result = hour[:2] + s[2:]
    else:
        s=s[:-2]
        result = s
        hour1 = int(s[0])
        hour2 = int(s[1])
        hour = hour1*10+hour2
        if hour >= 12:
            hour -= 12
            if hour < 10:
                hour = "0"+str(hour)
                print(hour)
            else:
                hour = str(hour)
            result = hour[:2] + s[2:]     
            print(result)
        else:
            result = s
                
    return result
    

if __name__ == '__main__':

    s = "12:45:54PM"

    result = timeConversion(s)

    print(result)