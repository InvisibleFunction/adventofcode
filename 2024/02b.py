#!/usr/bin/env python3

import os
import sys
inFile = sys.argv[1]
from icecream import ic

with open(inFile,'r') as f:
    lines = f.read().splitlines()

reports = []
for line in lines:
    items = line.split(' ')
    reports.append([int(x) for x in items])

ic(reports)

def diff_report(report):
    diff_report = []
    for i in range(len(report)-1):
        diff_report.append(report[i] - report[i+1])
#    ic(diff_report)
    return diff_report

def is_iord(report2):
    bmatch = 0 < report2[0]
#    ic(bmatch)
    running = True
    for i in report2:
        if bmatch == (0 < i):
            pass
        else:
            return False
    return True

def is_limited(report):
    report2 = [abs(x) for x in report]
    ic(max(report2))
    ic(min(report2))
    return (max(report2) <= 3) and (min(report2) >= 1)

def check(dr):
    return is_iord(dr) and is_limited(dr)

is_ok = 0
for report in reports:
    ic(report)
    thistime = False
    for i in range(len(report)):
        ic(i)
        local = report.copy()
        local.pop(i)
        thistime = check(diff_report(local))
        if thistime:
            is_ok += 1
            break

ic(is_ok)


