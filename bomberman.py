#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
class Bomb():
    def __init__(self) -> None:
        self.timeToDetonation = 3

def detonate(grid, i, j):
    if i+1 < len(grid):
        if not isinstance(grid[i+1][j],Bomb):
            grid[i+1][j] = "."
        if isinstance(grid[i+1][j], Bomb) and grid[i+1][j].timeToDetonation != 1:
            grid[i+1][j] = "."
    if j+1 < len(grid[0]):
        if not isinstance(grid[i][j+1],Bomb):
            grid[i][j+1] = "."
        if isinstance(grid[i][j+1], Bomb) and grid[i][j+1].timeToDetonation != 1:
            grid[i][j+1] = "."
    if i-1 >= 0:
        grid[i-1][j] = "."
    if j-1 >= 0:
        grid[i][j-1] = "."
    grid[i][j]="."

def plantBombs(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not isinstance(grid[i][j], Bomb):
                grid[i][j] = Bomb()

def bomberMan(n, grid):
    # Write your code here
    
    if n <= 1:
        return grid
    
    n = n % 4 + 4
        
    for i in range(len(grid)):
        holdRow = []
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                holdRow.append(Bomb())
            else:
                holdRow.append(".")
        grid[i] = holdRow

    x = 0
    while x < n:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if isinstance(grid[i][j],Bomb):
                    grid[i][j].timeToDetonation -= 1
                    if grid[i][j].timeToDetonation == 0:
                        detonate(grid, i ,j)
        x += 1
        if x % 2 == 0:
            plantBombs(grid)

    for i in range(len(grid)):
        holdRow = ""
        for j in range(len(grid[i])):
            if isinstance(grid[i][j],Bomb):
                holdRow += "O"
            else:
                holdRow += "."
        grid[i] = holdRow

    return grid
    

if __name__ == '__main__':

    result = bomberMan(0, [".......","...O...","....O..",".......","OO.....","OO....."])
    for i in result:
        print(i)
    print("--------")
    result = bomberMan(4, [".......","...O...","....O..",".......","OO.....","OO....."])
    for i in result:
        print(i)
    print("--------")
    result = bomberMan(8, [".......","...O...","....O..",".......","OO.....","OO....."])
    for i in result:
        print(i)
    print("--------")
