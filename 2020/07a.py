#!/usr/bin/env python3

import os
import sys
import re
#from collections import defaultdict
inFile = sys.argv[1]

with open(inFile,'r') as f:
  lines = f.read().splitlines()

data = {}

for line in lines:
  print(line)  
  containing_color = re.sub(r' bags contain.*','',line)
  rules = re.sub(r'.* bags contain ','',line)
  data[containing_color] = []
  for prule in rules.split(','):
    print(prule)
    if prule == 'no other bags.': pass
    else:
      match = re.match(r'([0-9]*) (\D*) b',prule.strip())
      if match:
        data[containing_color].append(( match.group(1), match.group(2) ))
      else: sys.exit("oh shit")

print(data)

def colors_contained( color ):
  cc = set(())
  if data[color] == None: pass
  else:
    for i in data[color]:
      cc.add( i[1] )
      cc = cc | colors_contained( i[1] )
  return cc

data2 = {}
for color in data.keys():
  data2[color] = colors_contained( color )
print()
for d in data2.keys():
  print(f"{d}: {data2[d]}")

total = 0
for color in data2.keys():
  if "shiny gold" in data2[color]:
    total = total + 1

print(total)
