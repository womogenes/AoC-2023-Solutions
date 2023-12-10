with open("./day_10.in") as fin:
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


dirs = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}


def get_dnbrs(i, j):
    res = []
    if lines[i][j] == "S":
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ii, jj = i + di, j + dj
            didjs = []  # Values of di and dj that link up
            if not (0 <= ii < n and 0 <= jj < m):
                continue

            if (i, j) in list(get_nbrs(ii, jj)):
                didjs.append((i, j))
                res.append((di, dj))

        # Find which character corresponds to this one
        # "ds" for "dirs"
        for char, ds in dirs.items():
            if sorted(ds) == sorted(didjs):
                break

        lines[i].replace("S", char)

        return res

    else:
        return dirs[lines[i][j]]


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
    count = 0
    for k in range(j):
        if not (i, k) in visited:
            continue
        count += line[k] in {"J", "L", "|"}

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
