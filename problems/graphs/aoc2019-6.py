"""
Starter code for Advent of Code 2019 Day #6
You must implement functions part1 and part2
"""

import sys
import os
import re


def part1(orbits):
    """
    Solves Part 1 (see problem statement for more details)
    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")
    Returns an integer

    Takeaways:
    DFS should operate on the current node.
    Perform an operation on the current node, and collect results from child nodes.
    """
    ### Replace with your code
    for child,parent in orbits.items():
        if parent not in orbits:
            current = parent
            break
    total = 0
    total,visited =  _findpaths(set(), current, orbits, total)
    return total

def _findpaths(visited, current, orbits, depth = 0):
    total = 0
    if current in visited:
        return (0, visited)
    visited.add(current)
    total += depth
    if current not in orbits.values():
        return (total, visited)
    for child,parent in orbits.items():
        if parent == current:
            sumchildren,visited = _findpaths(visited, child, orbits, depth+1)
            total += sumchildren
    return (total,visited)

class Node:
    def __init__(self, name, adj):
        self.name = name
        self.adjacent = adj

def part2(orbits):
    """
    Solves Part 2 (see problem statement for more details)
    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")
    Returns an integer
    """
    ### Replace with your code
    start = orbits["YOU"]
    counter = 0
    queue = []
    queue.append((start,counter))
    visited = {start}
    while len(queue) > 0:
        current = queue.pop(0)
        visited.add(current[0])
        neighbors = []
        for key,val in orbits.items(): #this searches for non-main orbitals
            if val == current[0]:
                neighbors.append((key,current[1]+1))
        try:
            neighbors.append((orbits[current[0]], current[1]+1)) #this searches for main orbitals
        except KeyError:
            pass
        for keyn, countern in neighbors:
            if keyn not in visited:
                if keyn == "SAN":
                    return countern-1
                queue.append((keyn,countern))
    return None

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
        objs = [line.split(")") for line in lines]
        orbits = {}
        for p1, p2 in objs:
            orbits[p2] = p1

    print(f"Part 1:", part1(orbits))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(orbits))
