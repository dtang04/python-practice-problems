"""
Starter code for Advent of Code 2022 Day #21
You must implement functions part1 and part2
"""

import sys
import os


def part1(monkeys):
    """
    Solves Part 1 (see problem statement for more details)
    Parameter:
    - monkeys: A dictionary mapping monkey names to a list of
      strings representing what the monkey "shouts".
      If the list contains a single string, it will represent
      an integer. If it contains three strings, it represents
      an arithmetic operation. For example:
        {'root': ['pppw', '+', 'sjmn'],
         'dbpl': ['5'],
         'cczh': ['sllz', '+', 'lgvd']}
    Returns an integer
    """
    return solve(monkeys, "root")

def solve(monkeys, key):
    if len(monkeys[key]) == 1:
        return int(monkeys[key][0])
    else:
        m1 = monkeys[key][0]
        op = monkeys[key][1]
        m2 = monkeys[key][2]
        if op == "+":
            return solve(monkeys,m1) + solve(monkeys,m2)
        if op == "-":
            return solve(monkeys,m1) - solve(monkeys,m2)
        if op  == "*":
            return solve(monkeys,m1) * solve(monkeys,m2)
        return solve(monkeys,m1) / solve(monkeys,m2)

def part2(monkeys):
    """
    Solves Part 2 (see problem statement for more details)
    Parameter:
    - monkeys: Same as Part 1.
    Returns an integer
    """
    half2 = monkeys["root"][2]
    match = solve(monkeys, half2)
    half1 = monkeys["root"][0]
    val = -20000
    res = solve2(val,half1,monkeys)
    status = False
    prev = False
    amount_to_add = 10000000000000
    counter = 0
    while res != match:
        counter += 1
        resid = res - match
        if resid > 0:
            status = False
            val += amount_to_add
        elif resid < 0:
            status = True
            val -= amount_to_add
        if status != prev:
            prev = status
            amount_to_add = amount_to_add/10
        res = solve2(val,half1,monkeys)
    return val

def solve2(val,key,monkeys):
    if key == "humn":
        return val
    if len(monkeys[key]) == 1:
        return int(monkeys[key][0])
    else:
        m1 = monkeys[key][0]
        op = monkeys[key][1]
        m2 = monkeys[key][2]
        if op == "+":
            return solve2(val,m1,monkeys) + solve2(val,m2,monkeys)
        if op == "-":
            return solve2(val,m1,monkeys) - solve2(val,m2,monkeys)
        if op == "*":
            return solve2(val,m1,monkeys) * solve2(val,m2,monkeys)
        return solve2(val,m1,monkeys) / solve2(val,m2,monkeys)

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
        lines = [line.split(": ") for line in f.read().split("\n")]
        monkeys = {}
        for monkey, message in lines:
            monkeys[monkey] = message.split()

    print(f"Part 1:", part1(monkeys))
    
    # Uncomment the following line when you're ready to work on Part 2
    print(f"Part 2:", part2(monkeys))