from collections import defaultdict
import re

with open("./day_08.in") as fin:
    lines = fin.read().strip().split("\n")

children = defaultdict(str)

steps = lines[0]
for line in lines[2:]:
    par, left, right = re.search("(...) = \((...), (...)\)", line).groups(0)
    children[par] = (left, right)

cur = "AAA"
count = 0
while cur != "ZZZ":
    step = steps[count % len(steps)]
    if step == "L":
        cur = children[cur][0]
    else:
        cur = children[cur][1]

    count += 1

print(count)
