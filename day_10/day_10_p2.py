from functools import lru_cache
from collections import deque

with open("./day_10_2.in") as fin:
    lines = fin.read().strip().split("\n")

n, m = len(lines), len(lines[0])

# Time for graph shenanigans
# Construct adjacency graph


def get_nbrs(i, j):
    res = []
    for di, dj in list(get_dnbrs(i, j)):
        ii, jj = i + di, j + dj
        if not (0 <= ii < n and 0 <= jj < m):
            continue
        res.append((ii, jj))
    return res


def get_dnbrs(i, j):
    res = []
    if lines[i][j] == "S":
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ii, jj = i + di, j + dj
            if not (0 <= ii < n and 0 <= jj < m):
                continue

            if (i, j) in list(get_nbrs(ii, jj)):
                res.append((di, dj))
        return res

    else:
        res = {
            "|": [(1, 0), (-1, 0)],
            "-": [(0, 1), (0, -1)],
            "L": [(-1, 0), (0, 1)],
            "J": [(-1, 0), (0, -1)],
            "7": [(1, 0), (0, -1)],
            "F": [(1, 0), (0, 1)],
            ".": [],
        }[lines[i][j]]
        return res


si, sj = None, None
for i, line in enumerate(lines):
    if "S" in line:
        si, sj = i, line.index("S")
        break


# Do a BFS
visited = set()
coords = []
dists = {}
stack = [(si, sj)]
while len(stack) > 0:
    top = stack.pop()
    if top in visited:
        continue
    visited.add(top)
    coords.append(top)

    for nbr in list(get_nbrs(*top)):
        if nbr in visited:
            continue
        stack.append(nbr)


# Count the number of "inversions" in a row
def count_invs(i, j):
    # Everything up to (but not including) j in line i
    line = lines[i]

    k = 0
    count = 0
    while k < j:
        if (i, k) not in visited:
            k += 1
            continue

        if line[k] == "|":
            count += 1
            k += 1
            continue

        if line[k] == "L":
            k += 1
            while line[k] == "-":
                k += 1
            if line[k] == "7":
                count += 1
            k += 1
            continue

        if line[k] == "F" or line[k] == "S":
            k += 1
            while line[k] == "-":
                k += 1
            if line[k] == "J":
                count += 1
            k += 1
            continue

        k += 1

    return count


ans = 0
for i, line in enumerate(lines):
    for j in range(m):
        if not (i, j) in visited:
            invs = count_invs(i, j)
            if invs > 0:
                # print(i, str(j).ljust(3), str(invs).ljust(
                # 5), line, line[j], end="  ")
                if invs % 2 == 1:
                    # print("*****", end="")
                    ans += 1
                # print()

print(ans)
