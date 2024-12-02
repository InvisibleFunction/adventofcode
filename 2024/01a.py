#!/usr/bin/env python3

import os
import sys
inFile = sys.argv[1]
from icecream import ic

with open(inFile,'r') as f:
    lines = f.read().splitlines()

l1 = []
l2 = []
for line in lines:
  t = line.split()
  l1.append(t[0])
  l2.append(t[-1])

ic(l1,l2)
l1.sort()
l2.sort()
ic(l1,l2)
d = 0
for i in range(0,len(l1)):
    ic(i)
    d += abs(int(l1[i])-int(l2[i]))

ic(d)
    

