#!/usr/bin/env python3

import os
import sys
import re
from collections import defaultdict
inFile = sys.argv[1]

with open(inFile,'r') as f:
  lines = f.read().splitlines()

data = []
gno = 0
mno = 0
falselist = []
for i in range(0,26):
  falselist.append(False)

for line in lines:
  if len(data) <= gno:
    data.append([])
  if line:
    data[gno].append(falselist.copy())
  for char in line:
    pos = ord(char) - 97
    data[gno][mno][pos] = True
  if not line:
    gno = gno + 1
    mno = 0
  else:
    mno = mno + 1

print(data)

tt = 0
for group in data:
  print('g')
  print(group)
  grouplist = falselist.copy()
  for i in range(0,26):
    for glist in group:
      if glist[i]: grouplist[i] = True
  grouptotal = 0
  for i in range(0,26):
    if grouplist[i]: grouptotal = grouptotal+1
  print(grouptotal)
  tt = tt + grouptotal

print(tt)
    
