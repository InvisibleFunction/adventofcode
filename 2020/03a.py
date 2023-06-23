#!/usr/bin/env python3

import os
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
  lines = f.read().splitlines()

data = []
for line in lines:
  linedata = []
  for character in line:
    if character == '#': linedata.append(True)
    else: linedata.append(False)
  data.append(linedata)

slope = (3, 1)
pos = 0
count = 0
for line in data:
  if line[pos % len(line)]: count = count+1
  pos = pos + slope[0]

print(count)
