import re

with open("day_04.in") as fin:
    lines = fin.read().strip().split("\n")


n = len(lines)
copies = [[] for _ in range(n)]

for i, line in enumerate(lines):
    parts = re.split("\s+", line)
    idx = parts.index("|")
    winning = list(map(int, parts[2:idx]))
    ours = list(map(int, parts[idx+1:]))

    score = 0
    for num in ours:
        if num in winning:
            score += 1

    for j in range(i+1, i+score+1):
        copies[i].append(j)


score = [1 for _ in range(n)]

for i in range(n-1, -1, -1):
    for j in copies[i]:
        score[i] += score[j]

print(sum(score))
