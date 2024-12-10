#!/usr/bin/env python3

from collections import defaultdict
from icecream import ic
import os
import re
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
    lines = f.read().splitlines()
ic.disable()
ic(lines)

visited = set()
grid = defaultdict(int)
obs = defaultdict(int)
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

def in_grid(xgrid, xguard):
    return xguard["pos"][0] >= 0 and xguard["pos"][0] < xgrid["maxx"] and xguard["pos"][1] >= 0 and xguard["pos"][1] < xgrid["maxy"]

def whats_in_front(wgrid, wguard):
    next_pos = (wguard["pos"][0] + dm[wguard["d"]][0], wguard["pos"][1] + dm[wguard["d"]][1])
    #ic(next_pos)
    return wgrid[next_pos]

def move_guard(mgrid, mguard):
    in_front = whats_in_front(mgrid,mguard)
    if in_front == 0:
        mguard["pos"] = ( mguard["pos"][0] + dm[mguard["d"]][0], mguard["pos"][1] + dm[mguard["d"]][1])
    elif in_front == 1:
        mguard["d"] = (mguard["d"] + 1) % 4
    else:
        print("uh oh 3")
        ic(mguard)
    return mgrid, mguard

#while in_grid(grid, guard):
#    visited.add(guard["pos"])
#    grid, guard = move_guard(grid, guard)

def is_loop(igrid, iguard):
    visited = defaultdict(int)
    ic(visited)
    ic(iguard)
    while in_grid(igrid, iguard):
        if visited and max(visited.values()) > 10:
            ic("t")
            return True
        visited[iguard["pos"]] += 1
        igrid, iguard = move_guard(igrid, iguard)
    ic("f")
    ic(visited)
    return False

loopcount = 0
for x2 in range(grid["maxx"]):
    for y2 in range(grid["maxy"]):
        ic(x2,y2)
        lgr = grid.copy()
        lgr[(x2,y2)] = 1
        draw_grid(lgr)
        lgu = guard.copy()
        if is_loop(lgr,lgu):
            ic("yes loop")
            loopcount += 1

        
ic("end")
ic(loopcount)
print(loopcount)
