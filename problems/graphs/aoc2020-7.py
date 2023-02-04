"""
Starter code for Advent of Code 2020 Day #7
You must implement functions part1 and part2
"""

import sys
import os
import re


def part1(rules):
    """
    Solves Part 1 (see problem statement for more details)
    Parameter:
    - rules: a dictionary mapping colors to a list
             of (color, amount)
    Returns an integer
    """
    ### Replace with your code
    queue = []
    numcombinations = 0
    counter = 0
    lst = []
    queue.append("shiny gold")
    uniquecols = set()
    while len(queue) > 0:
        current = queue.pop(0)
        for colors in rules:
            for color in rules[colors]:
                if current in color:
                    uniquecols.add(colors)
                    queue.append(colors)
    return len(uniquecols)


def part2(rules):
    """
    Solves Part 2 (see problem statement for more details)
    Parameter:
    - rules: a dictionary mapping colors to a list
             of (color, amount)
    Returns an integer
    """
    stack = []
    numcombinations = 0
    counter = 0
    lst = []
    stack.append("shiny gold")
    counter = 0
    print(rules)
    while len(stack) > 0:
        print(stack, counter)
        current = stack.pop(0)
        print(current)
        flag = False
        for colors in rules:
            if current == colors:
                for color,num in rules[current]:
                    counter += num
                    for i in range(num):
                        stack.insert(0,color)
    return counter

############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################

def read_rules(lines):
    """
    Given the text input, convert it to a graph-like structure.
    Specifically, a dictionary mapping colors to a list of (color, amount)
    tuples.
    """

    rules = {}

    for line in lines:
        m = re.match("(.*) bags contain (.*)\.", line)
        container_bag, contained_bags = m.groups()

        if contained_bags == "no other bags":
            bags = []
        else:
            bags = []
            bag_strs = contained_bags.split(", ")
            for bag in bag_strs:
                amount, color1, color2, _ = bag.split()
                bags.append((f"{color1} {color2}", int(amount)))

        rules[container_bag] = bags

    return rules

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
        rules = read_rules(lines)

    print(f"Part 1:", part1(rules))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(rules))