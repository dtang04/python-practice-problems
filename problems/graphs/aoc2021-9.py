"""
Starter code for Advent of Code 2021 Day #9
You must implement functions part1 and part2
"""

import sys
import os
import re


def part1(grid):
    """
    Solves Part 1 (see problem statement for more details)
    Parameter:
    - grid: a list of lists of integers representing
            a heightmap
    Returns an integer
    """
    ### Replace with your code
    sums = 0
    for i,_ in enumerate(grid):
        for j,_ in enumerate(grid[i]):
            if determine_lowest(grid,i,j):
                sums += grid[i][j]+1
    return sums
    
def determine_lowest(grid,i,j):
    lst = [grid[i][j]]
    if i - 1 >= 0:
        lst.append(grid[i-1][j])
    if i + 1 < len(grid):
        lst.append(grid[i+1][j])
    if j - 1 >= 0:
        lst.append(grid[i][j-1])
    if j + 1 < len(grid[i]):
        lst.append(grid[i][j+1])
    if grid[i][j] == min(lst) and lst.count(grid[i][j]) == 1:
        return True
    return False


def part2(grid):
    """
    Solves Part 2 (see problem statement for more details)
    Parameter:
    - grid: a list of lists of integers representing
            a heightmap
    Returns an integer
    """
    mins = []
    for i,_ in enumerate(grid):
        for j,_ in enumerate(grid[i]):
            if determine_lowest(grid,i,j):
               mins.append((i,j))
    visited = set()
    size = 1
    lst = []
    for tup in mins:
        stemp,_ = _determinebasinsize(visited,tup[0],tup[1],grid)
        lst.append(stemp)
    for _ in range(3):
        size *= max(lst)
        del lst[lst.index(max(lst))]
    return size

def _determinebasinsize(visited, row, col, grid):
    size = 1
    visited.add((row,col))
    #print(visited, "current: " +  str(grid[row][col]), "location: " + str(row) + " " + str(col))
    if row - 1 >= 0 and grid[row][col] < grid[row-1][col] and (row-1, col) not in visited and grid[row-1][col] != 9:
        up, vup = _determinebasinsize(visited, row - 1, col, grid)
        size += up
        visited.union(vup)
    if row + 1 < len(grid) and grid[row][col] < grid[row+1][col] and (row+1, col) not in visited and grid[row+1][col] != 9:
        down,vdown = _determinebasinsize(visited, row + 1, col, grid)
        size += down
        visited.union(vdown)
    if col - 1 >= 0 and grid[row][col] < grid[row][col-1] and (row, col-1) not in visited and grid[row][col-1] != 9:
        left,vleft = _determinebasinsize(visited, row, col - 1, grid)
        size += left
        visited.union(vleft)
    if col + 1 < len(grid[row]) and grid[row][col] < grid[row][col+1] and (row, col+1) not in visited and grid[row][col+1] != 9:
        right,vright = _determinebasinsize(visited, row, col + 1, grid)
        size += right
        visited.union(vright)
    return (size,visited)

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
            grid.append([int(c) for c in line])

    #print(f"Part 1:", part1(grid))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(grid))