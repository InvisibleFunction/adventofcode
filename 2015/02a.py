from icecream import ic
import sys
import itertools

filename = sys.argv[1]
ic(filename)

lines = []
with open(filename) as file:
    while (line := file.readline().rstrip()):
        lines.append(line)
ic(lines)

def find_area( s ):
    d = [int(x) for x in s.split("x")]
    ic(d)
    d2 = []
    for c in itertools.combinations(d, 2):
        ic(c)
        d2.append(c[0] * c[1] )
    ic(d2)
    d2.sort()
    
    ans = (d2[0] * 3) + (d2[1] * 2) + (d2[2] * 2)
    return ans


sum = 0
for line in lines:
    sum += find_area(line)

ic(sum)
