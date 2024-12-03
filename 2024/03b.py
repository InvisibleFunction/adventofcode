#!/usr/bin/env python3

from icecream import ic
import os
import re
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
    lines = f.read().splitlines()
myinput = ""
for line in lines:
    myinput = myinput + " " + line

mysum = 0
pattern1 = r"don\'t\(\).*?do\(\)"
input2 = re.sub(pattern1, "", myinput)
pattern2 = r"don\'t\(\).*$"
input3 = re.sub(pattern2, "", input2)
pattern3 = r"mul\((-?\d+),(-?\d+)\)"
matches = re.findall(pattern3, input3)
for match in matches:
    mysum += int(match[0]) * int(match[1])

ic(mysum)


