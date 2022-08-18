#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribesOld(q):
    # Write your code here
    orderedQDict = {}
    for i in range(len(q)):
        orderedQDict[q[i]] = i + 1
    q1= q[:]
    bribeCount = 0
    bribeCount1 = 0
    count = 0
    for i in range(len(q),0,-1):
        dif1 = i - q1.index(i) - 1
        if  dif1 > 2:
            print("Too chotic")
            return
        else:
            bribeCount1 += dif1
        q1.remove(i)

        dif = i - orderedQDict[i]
        if  dif > 2:
            print("Too chaotic")
            return
        else:
            bribeCount += dif
        for i in range(orderedQDict[i],len(q)):
            orderedQDict[q[i]] -= 1

    print(bribeCount)

def minimumBribes(q):
    bribeCount = 0
    for i in range(len(q),0,-1):
        dif = i - q.index(i) - 1
        if  dif > 2:
            print("Too chaotic")
            return
        else:
            bribeCount += dif
        q.remove(i)

    print(bribeCount)


if __name__ == '__main__':


    q = [1,2,5,3,7,8,6,4]
    minimumBribesOld(q)
