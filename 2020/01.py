#!/usr/bin/env python3

import os
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
    lines = f.read().splitlines()

nos = []
for line in lines:
  nos.append(int(line))

print(nos)
for line in nos:
  nos.remove(line)
  for num in nos:
    sl = nos.copy()
    sl.remove(num)
    missingno = 2020 - line - num
    #print("missing: {}".format(missingno))
    if missingno in sl:
      print("ANSWER: {}".format( line * num * missingno))


