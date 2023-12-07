from functools import cmp_to_key
from collections import defaultdict

with open("./day_07.in") as fin:
    raw_lines = fin.read().strip().split("\n")


labels = "AKQT98765432J"


def get_type(hand):
    counts = defaultdict(int)
    jokers = 0
    for x in hand:
        if x == "J":
            jokers += 1
        else:
            counts[x] += 1

    amounts = sorted(counts.values())
    if jokers >= 5 or amounts[-1] + jokers >= 5:
        return 5
    if jokers >= 4 or amounts[-1] + jokers >= 4:
        return 4

    # Try a full house
    if amounts[-1] + jokers >= 3:
        rem_jokers = amounts[-1] + jokers - 3
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 3.5
        return 3

    if amounts[-1] + jokers >= 2:
        rem_jokers = amounts[-1] + jokers - 2
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 2.5
        return 2

    return 1

# We need to sort these


def compare(a, b):
    # a and b are two hands
    rankA = (get_type(a), a)
    rankB = (get_type(b), b)
    if rankA[0] == rankB[0]:
        if a == b:
            return 0
        for i, j in zip(a, b):
            if labels.index(i) < labels.index(j):
                return 1
            if labels.index(i) > labels.index(j):
                return -1
        return -1
    if rankA[0] > rankB[0]:
        return 1
    return -1


lines = []
for line in raw_lines:
    line = line.split()
    lines.append((line[0], int(line[1])))


lines = sorted(lines, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))
ans = 0
for i, line in enumerate(lines):
    ans += (i + 1) * line[1]

print(ans)
