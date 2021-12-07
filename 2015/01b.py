from icecream import ic
import sys


filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
ic(lines)

def how_many_floors( s ):
    return s.count("(") - s.count(")")

def pos_to_basement( s ):
    elev = 0
    for i, c in enumerate(s):
        ic(i,c)
        if c == "(":
            elev += 1
        elif c == ")":
            elev -= 1
        if elev < 0:
            return i + 1


for line in lines:
    print(pos_to_basement(line))
