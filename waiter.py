#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def isPrime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True

def primeList(q):
    primeList = []
    count = 0
    i = 2
    while count < q:
        if isPrime(i):
            primeList.append(i)
            count += 1
        i += 1
    return primeList

def waiter(number, q):
    # Write your code here
    answers = []
    a = number
    pList = primeList(q)

    count = 0
    for i in pList:
        a1 = []
        count +=1
        for j in a:
            if j % i == 0:
                answers.append(j)
            else:
                a1.append(j)
        a1.reverse()
        print("A",count,":",a1)
        print(answers)
        a = a1
    a.reverse()
    for i in a:
        answers.append(i)

    return answers

if __name__ == '__main__':
    #print(waiter([2,3,4,5,6,7],3))
    print(waiter([3,4,7,6,5],1))
