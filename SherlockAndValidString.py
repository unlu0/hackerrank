#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    charDict = dict()
    for i in s:
        if charDict.get(i) is None:
            charDict[i] = 1 
        else:
            charDict[i] += 1


    charDictValues = list(charDict.values())
    charCountDict = dict()

    for i in charDictValues:
        if charCountDict.get(i) is None:
            charCountDict[i] = 1
        else:
            charCountDict[i] += 1
        
    charCountDictKeys = list(charCountDict.keys())
    if len(charCountDictKeys) > 2:
        return "NO"
    elif len(charCountDictKeys) == 2:
        if charCountDict[charCountDictKeys[0]] == 1 and charCountDictKeys[0] == 1:
            return "YES"
        if charCountDict[charCountDictKeys[1]] == 1 and charCountDictKeys[1] == 1:
            return "YES"
        if charCountDict[charCountDictKeys[0]] == 1 or charCountDict[charCountDictKeys[1]] == 1:
            if charCountDictKeys[0] == 1 or charCountDictKeys[1] == 1:
                if abs(charCountDictKeys[0]-charCountDictKeys[1]) > 1:
                    return "NO"
                else:
                    return "YES"
            if abs(charCountDictKeys[0]-charCountDictKeys[1]) > 1:
                return "NO"
            else:
                return "YES"
        else:
            return "NO"

    return "YES"

if __name__ == '__main__':

    s = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd"
    

    result = isValid(s)

    print(result)
