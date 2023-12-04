import re

with open("day_04.in") as fin:
    lines = fin.read().strip().split("\n")

ans = 0

for line in lines:
    parts = re.split("\s+", line)
    winning = list(map(int, parts[2:12]))
    ours = list(map(int, parts[13:]))

    score = 0
    for num in ours:
        if num in winning:
            score += 1

    if score > 0:
        ans += 2**(score - 1)

print(ans)
