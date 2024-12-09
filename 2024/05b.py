#!/usr/bin/env python3

from collections import Counter
from collections import defaultdict
from icecream import ic
import os
import re
import sys
inFile = sys.argv[1]

#ic.disable()

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
for page in pages:
    assert len(page) % 2 == 1


def order_it(pages, lrules):
    if not pages:
        print("uh oh 1")
        sys.exit(1)
    if len(pages) == 0:
        print("uh oh")
        sys.exit(1)
    if len(pages) == 1:
        return pages
    page_list = []
    for rule in lrules:
        page_list.append(rule[0])
    counter = Counter(page_list)
    most_common = counter.most_common(1)[0][0]
    if most_common in pages:
        pages.remove(most_common)
        return [most_common] + order_it(pages, [t for t in lrules if most_common not in t])
    else:
        return order_it(pages, [t for t in lrules if most_common not in t])

def order_it_ka(lpages, lrules):
    indegree = defaultdict(int)
    graph = defaultdict(set)
    for i, j in lrules:
        if i in lpages and j in lpages:
            graph[i].add(j)
            indegree[j] += 1
            indegree.setdefault(i,0)

    ic(indegree)
    ic(graph)

    queue = [n for n in lpages if indegree[n] == 0]
    sorted_pages = []
    while queue:
        n = queue.pop()
        sorted_pages.append(n)
        for m in graph[n]:
            indegree[m] -= 1
            if indegree[m] == 0:
                queue.append(m)
    return sorted_pages


my_sum = 0
my_sum2 = 0
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
    else:
        ic("Out of order: ",pags)
        ordered_pags = order_it_ka(pags, rules.copy())
        ic(ordered_pags)
        my_sum2 += int(ordered_pags[int((len(ordered_pags) - 1)/2)])

ic(my_sum)
ic(my_sum2)
print(my_sum2)
