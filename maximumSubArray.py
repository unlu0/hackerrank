#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def maxSumOlder(arr,start,end,maxSumOfArr,result):
    if start == end:
        return
    
    maxSumLeft = maxSumOfArr - arr[start]
    maxSumRight = maxSumOfArr - arr[end]
    if maxSumLeft > result[0]:
        result[0] = maxSumLeft
    if maxSumRight > result[0]:
        result[0] = maxSumRight
    
    maxSum(arr,start+1,end,maxSumLeft,result)
    maxSum(arr,start,end-1,maxSumRight,result) 

def maxSumNew(arr):
    maxSum = -sys.maxsize
    sumTemp = 0
    for i in range(1,len(arr)+1):
        sumTemp += arr[i-1]
        maxSumTemp = sumTemp
        if maxSumTemp > maxSum:
            maxSum = maxSumTemp
        j = i
        t = 0
        while j < len(arr):
            maxSumTemp = maxSumTemp - arr[t] + arr[j]
            j += 1
            t += 1
            if maxSumTemp > maxSum:
                maxSum = maxSumTemp
    return maxSum

def maxSum(arr):
    maxSum = -sys.maxsize
    maxEndingHere = 0
    for i in arr:
        maxEndingHere +=i
        if maxEndingHere > maxSum:
            maxSum = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0

    return maxSum

def maxSumOld(arr):
    maxSum = sum(arr)
    maxSumOfArr = maxSum
    start = 0
    end = len(arr)-1
    count = 0
    while start != end:
        maxSumLeft = maxSumOfArr - arr[start]
        maxSumRight = maxSumOfArr - arr[end]
        if maxSumLeft > maxSum:
            maxSum = maxSumLeft
        if maxSumRight > maxSum:
            maxSum = maxSumRight
        count +=1
        if count % 2 == 0:
            start += 1
        else:
            end -= 1
    

    

def maxSubarray(arr):
    # Write your code here
    #result = [sum(arr)]
    #maxSum(arr,0,len(arr)-1,sum(arr),result)
    result = maxSum(arr)
    subseqSum = 0
    for i in arr:
        if i > 0:
            subseqSum += i
    if subseqSum == 0:
        subseqSum += max(arr)
    
    return result,subseqSum
    

if __name__ == '__main__':
    arr = "2 -1 2 3 4 -5"
    arr = list(map(int,arr.split()))
    print(maxSubarray(arr))
