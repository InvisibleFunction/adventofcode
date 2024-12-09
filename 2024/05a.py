#!/usr/bin/env python3

from icecream import ic
import os
import re
import sys
inFile = sys.argv[1]

with open(inFile,'r') as f:
    lines = f.read().splitlines()
rules = []
pages = []
pagesMarker = False
for line in lines:
    if not line:
        pagesMarker = True
    elif not pagesMarker:
        rules.append(tuple(line.split("|")))
    else:
        pages.append(line.split(","))

ic(rules)
ic(pages)

my_sum = 0
for pags in pages:
    inOrder = True
    for rule in rules:
        if all(x in pags for x in rule):
            if pags.index(rule[0]) < pags.index(rule[1]):
                pass
            else:
                inOrder = False
    if inOrder:
        my_sum += int(pags[int((len(pags) - 1)/2)])
    ic(pags, inOrder)

ic(my_sum)
