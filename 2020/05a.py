#!/usr/bin/env python3

import os
import sys
import re
inFile = sys.argv[1]

with open(inFile,'r') as f:
  lines = f.read().splitlines()

def find_seat( myin ):
  rowp = []
  for i in range(0,128):
    rowp.append(i)
  colp = []
  for i in range(0,8):
    colp.append(i)
  for chara in myin:
    match = re.search(r'[F,B]', chara)
    if match:
      mi = len(rowp) // 2
      rematch = re.search(r'[F]', chara)
      if rematch:
        rowp = rowp[:mi]
      else:
        rowp = rowp[mi:]
    else:
      mi = len(colp) // 2
      rematch = re.search(r'[L]', chara)
      if rematch:
        colp = colp[:mi]
      else:
        colp = colp[mi:]
  return (rowp[0], colp[0])


data = []
for line in lines:
  data.append(find_seat(line))

print(data)
highest = 0
for datum in data:
  sid = ( datum[0] * 8 ) + datum[1] 
  if sid > highest: highest = sid

print(highest)
