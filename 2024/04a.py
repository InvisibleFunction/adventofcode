#!/usr/bin/env python3

from icecream import ic
import os
import re
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
    lines = f.read().splitlines()

ic(lines)

dm={0:(0,-1),1:(1,-1),2:(1,0),3:(1,1),4:(0,1),5:(-1,1),6:(-1,0),7:(-1,-1)}
ic(dm)

def findit(loc,lines,d,s):
    if loc[0] < 0 or loc[0] >= len(lines[0]) or loc[1] < 0 or loc[1] >= len(lines):
        return False
    if len(s) == 1:
        return lines[loc[1]][loc[0]] == s
    elif s[0] == lines[loc[1]][loc[0]]:
        return findit((loc[0]+d[0],loc[1]+d[1]),lines,d,s[1:])
    else:
        return False

def findxmases(loc,lines):
    assert lines[loc[1]][loc[0]] == "X"
    lsum = 0
    for d in dm:
        if findit(loc,lines,dm[d],"XMAS"):
            lsum += 1
    return lsum




mysum = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == 'X':
            ic((x,y))
            mysum += findxmases((x,y),lines)

ic(mysum)
