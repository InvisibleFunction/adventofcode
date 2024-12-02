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
  l1.append(int(t[0]))
  l2.append(int(t[-1]))

ic(l1,l2)

#l1.sort()
#l2.sort()
#ic(l1,l2)
s = 0
for i in l1:
    ic(i)
    s += i * l2.count(i) 
    

ic(s)
    

