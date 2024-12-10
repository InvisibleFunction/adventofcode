#!/usr/bin/env python3

from collections import defaultdict
from icecream import ic
import os
import re
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
    lines = f.read().splitlines()

ic(lines)

visited = set()
grid = defaultdict(int)
grid["maxx"] = len(lines[0])
grid["maxy"] = len(lines)
guard = {}
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c == ".":
            grid[(x,y)] = 0
        elif c == "#":
            grid[(x,y)] = 1
        else:
            ic(c)
            grid[(x,y)] = 0
            guard["pos"] = (x,y)
            if c == "^":
                guard["d"] = 0
            elif c == ">":
                guard["d"] = 1
            elif c == "v":
                guard["d"] = 2
            elif c == "<":
                guard["d"] = 3
            else:
                print("uh oh")
                sys.exit(1)

dm = { 0: (0,-1), 1: (1, 0), 2: (0, 1), 3: (-1, 0) }
        
def draw_grid(grid, guard=None):
    for y in range(grid["maxy"]):
        line = ""
        for x in range(grid["maxx"]):
            if grid[(x,y)] == 0:
                line += "."
            elif grid[(x,y)] == 1:
                line += "#"
            else:
                if guard:
                    if guard["d"] == 0:
                        line += "^"
                    elif guard["d"] == 1:
                        line += ">"
                    elif guard["d"] == 2:
                        line += "v"
                    elif guard["d"] == 3:
                        line += "<"
                    else:
                        print("uh oh 2")
                        sys.exit(1)
                else:
                    line += "X"
        print(line)

draw_grid(grid, guard)

def in_grid(grid, guard):
    return guard["pos"][0] >= 0 and guard["pos"][0] < grid["maxx"] and guard["pos"][1] >= 0 and guard["pos"][1] < grid["maxy"]

def whats_in_front(grid, guard):
    next_pos = (guard["pos"][0] + dm[guard["d"]][0], guard["pos"][1] + dm[guard["d"]][1])
    ic(next_pos)
    return grid[next_pos]

def move_guard(grid, gaurd):
    in_front = whats_in_front(grid,guard)
    if in_front == 0:
        guard["pos"] = ( guard["pos"][0] + dm[guard["d"]][0], guard["pos"][1] + dm[guard["d"]][1])
    elif in_front == 1:
        guard["d"] = (guard["d"] + 1) % 4
    else:
        print("uh oh 3")
        ic(guard)
    return grid, guard

while in_grid(grid, guard):
    visited.add(guard["pos"])
    grid, guard = move_guard(grid, guard)

ic("end")
ic(guard)
ic(len(visited))

                
