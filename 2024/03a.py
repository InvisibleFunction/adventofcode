#!/usr/bin/env python3

from icecream import ic
import os
import re
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
    lines = f.read().splitlines()

mysum = 0
for line in lines:
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(pattern, line)
    for match in matches:
        mysum += int(match[0]) * int(match[1])

ic(mysum)


