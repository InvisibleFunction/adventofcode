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

slopes = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = []
for slope in slopes:
  pos = 0
  count = 0
  for i in range(0,len(data),slope[1]):
    if data[i][pos % len(line)]: count = count+1
    pos = pos + slope[0]
  counts.append(count)
  print(count)

print()
cum=1
for count in counts:
  cum = cum*count

print(cum)
