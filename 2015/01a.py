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

for line in lines:
    print(how_many_floors(line))
