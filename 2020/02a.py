#!/usr/bin/env python3

import os
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
  lines = f.read().splitlines()

input = []
for line in lines:
  #print(line.split())
  sline = line.split()
  elem = {}
  elem['min'] = int(sline[0].split('-')[0])
  elem['max'] = int(sline[0].split('-')[1])
  elem['char'] = sline[1].replace(':', '')
  elem['pass'] = sline[2]
  #print(elem)
  input.append( elem.copy() )

print(input)

matching = 0

for ele in input:
  print(ele['pass'])
  occ = ele['pass'].count(ele['char'])
  print(occ)
  if occ >= ele['min'] and occ <= ele['max']:
    print(f"{ele['pass']} is valid")
    matching = matching + 1

print(f"Matching passwords: {matching}")
  
  

