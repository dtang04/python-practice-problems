"""
Starter code for Advent of Code 2022 Day #12
You must implement functions part1 and part2
"""

import sys
import os
import re


def part1(grid):
    """
    Solves Part 1 (see problem statement for more details)
    Parameter:
    - grid: a list of lists of single-characters strings
            representing a heightmap
    Returns an integer
    """
    srow,scol = _findstart(grid)
    visited = {(0,0)}
    queue = []
    if srow - 1 >= 0:
        queue.append((srow-1,scol,1))
    if srow + 1 < len(grid):
        queue.append((srow+1,scol,1))
    if scol - 1 >= 0:
        queue.append((srow,scol-1,1))
    if scol + 1 < len(grid[0]):
        queue.append((srow,scol+1,1))
    while len(queue) > 0:
        crow,ccol,numsteps = queue.pop(0)
        visited.add((crow,ccol))
        cchar = grid[crow][ccol]
        neighbors = []
        if crow - 1 >= 0:
            neighbors.append((crow-1,ccol,numsteps+1))
        if crow + 1 < len(grid):
            neighbors.append((crow+1,ccol,numsteps+1))
        if ccol - 1 >= 0:
            neighbors.append((crow,ccol-1,numsteps+1))
        if ccol + 1 < len(grid[crow]):
            neighbors.append((crow,ccol+1,numsteps+1))
        for arow,acol,num in neighbors:
            flag = False
            for i,(row,col,qnum) in enumerate(queue):
                if arow == row and acol == col and qnum <= num:
                    flag = True
            if flag:
                continue
            if (arow,acol) in visited:
                continue
            if grid[arow][acol] == "E" and cchar == "z":
                return num
            if ord(grid[arow][acol]) == ord(cchar) + 1 or ord(grid[arow][acol]) <= ord(cchar) and grid[arow][acol] != "E":
                queue.append((arow,acol,num))
    return None

def _findstart(grid):
    for i,_ in enumerate(grid):
        for j,_ in enumerate(grid[i]):
            if grid[i][j] == "S":
                return (i,j)
    return None

def part2(grid):
    """
    Solves Part 2 (see problem statement for more details)
    Parameter:
    - grid: a list of lists of single-characters strings
            representing a heightmap
    Returns an integer
    """
    lst = []
    rlst = []
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if grid[i][j] == "a":
                lst.append((i,j))
    for i,j in lst:
        queue = []
        queue.append((i,j,0))
        visited = {(i,j)}
        while len(queue) > 0:
            crow,ccol,numsteps = queue.pop(0)
            visited.add((crow,ccol))
            cchar = grid[crow][ccol]
            neighbors = []
            if crow - 1 >= 0:
                neighbors.append((crow-1,ccol,numsteps+1))
            if crow + 1 < len(grid):
                neighbors.append((crow+1,ccol,numsteps+1))
            if ccol - 1 >= 0:
                neighbors.append((crow,ccol-1,numsteps+1))
            if ccol + 1 < len(grid[crow]):
                neighbors.append((crow,ccol+1,numsteps+1))
            for arow,acol,num in neighbors:
                flag = False
                for i,(row,col,qnum) in enumerate(queue):
                    if arow == row and acol == col and qnum <= num:
                        flag = True
                if flag:
                    continue
                if (arow,acol) in visited:
                    continue
                if grid[arow][acol] == "E" and cchar == "z":
                    rlst.append(num)
                if ord(grid[arow][acol]) == ord(cchar) + 1 or ord(grid[arow][acol]) <= ord(cchar) and grid[arow][acol] != "E":
                    queue.append((arow,acol,num))
    rlst.append(part1(grid))
    return min(rlst)


############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        lines = f.read().strip().split("\n")
        grid = []
        for line in lines:
            grid.append([c for c in line])

    print(f"Part 1:", part1(grid))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(grid))
