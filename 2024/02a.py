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
    ic(diff_report)
    return diff_report

def is_iord(report):
    report2 = diff_report(report)
    bmatch = 0 < report2[0]
    ic(bmatch)
    running = True
    for i in report2:
        if bmatch == (0 < i):
            pass
        else:
            return False
    return True

def is_limited(report):
    report2 = diff_report(report)
    return (max(report2) < 3) and (min(report2) > 1)

is_ok = 0
for report in reports:
    ic(is_iord(report))
    ic(is_limited(report))
    if is_iord(report) and is_limited(report):
        is_ok += 1

ic(is_ok)


