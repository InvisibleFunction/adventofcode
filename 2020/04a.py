#!/usr/bin/env python3

import os
import sys
import re
inFile = sys.argv[1]

with open(inFile,'r') as f:
  lines = f.read().splitlines()

data = []
ppno = 0
for line in lines:
  if len(data) <= ppno: data.append({})
  for ele in line.split():
    data[ppno][ele.split(':')[0]] = ele.split(':')[-1]
  if not line: ppno = ppno + 1

#req = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

#print(data)

def validate_byr( myin ):
  byr = int(myin)
  if byr <1920: return False
  if byr >2002: return False
  else: return True

def validate_iyr( myin ):
  iyr = int(myin)
  if iyr < 2010: return False
  if iyr > 2020: return False
  else: return True

def validate_eyr( myin ):
  eyr = int(myin)
  if eyr < 2020: return False
  if eyr > 2030: return False
  else: return True

def validate_hgt( myin ):
  if myin.endswith("cm"):
    hgt = int(myin.replace("cm",""))
    if hgt < 150 or hgt > 193:
      return False
    else: return True
  if myin.endswith('in'):
    hgt = int(myin.replace("in",""))
    if hgt < 59 or hgt > 76:
      return False
    else: return True
  else: return False

def validate_hcl( myin ):
  hcl = myin
  match = re.search(r'^.[0-9a-fA-F]{6}$', hcl)
  if not match: return False
  else: return True

def validate_ecl( myin ):
  if myin in ["amb","blu","brn","gry","grn","hzl","oth"]: return True
  else: return False

def validate_pid( myin ):
  pid = myin
  match = re.search(r'^[0-9]{9}$', pid)
  if match: return True
  else: return False
  
nov = 0
for pp in data:
  #print(pp)
  valid = True
  for rex in req:
    if rex not in pp: valid = False
    if not valid: print("not valid a")
  if valid:  
    for rex in req:
      method = globals()[f"validate_{rex}"]
      if not method( pp[rex] ): valid = False
      if not valid: print(f"not valid {rex}")
  if valid == True: nov = nov+1
  #print(f"is valid: {valid}")

print(nov)
