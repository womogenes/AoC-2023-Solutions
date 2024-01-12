import sys
sys.setrecursionlimit(999999)

with open("./day_16.in") as fin:
    lines = fin.read().strip().split("\n")

"""
Direction key:
  1
2 . 0
  3
"""

N = len(lines)
M = len(lines[0])

d_pos = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def enter(i, j, d):
    """
    Enter tile @ row i, col j, direction d
    """
    if not (0 <= i < N and 0 <= j < M):
        return
    if ins[i][j][d]:
        return
    ins[i][j][d] = True

    tile = lines[i][j]

    # Pass through
    if tile == ".":
        out_dirs = [d]
    # Splitters
    # Use fancy XOR to cut down on redundancy
    elif tile in ["-", "|"]:
        if (d in [1, 3]) ^ (tile == "-"):
            out_dirs = [d]
        else:
            out_dirs = [(d + 1) % 4, (d + 3) % 4]
    # Mirrors
    elif tile == "/":
        out_dirs = [[1, 0, 3, 2][d]]
    elif tile == "\\":
        out_dirs = [[3, 2, 1, 0][d]]

    for out_d in out_dirs:
        ii = i + d_pos[out_d][0]
        jj = j + d_pos[out_d][1]
        enter(ii, jj, out_d)


def energy(i, j, d):
    """
    Max energy if enter from tile (i, j) with direction d
    """
    global ins

    count = 0
    ins = [[[False] * 4 for _ in range(M)] for _ in range(N)]
    enter(i, j, d)
    for i in range(N):
        for j in range(M):
            count += any(ins[i][j])

    return count


best = 0
for j in range(M):
    best = max(best, energy(0, j, 3))
for j in range(M):
    best = max(best, energy(N - 1, j, 1))
for i in range(N):
    best = max(best, energy(i, 0, 0))
for i in range(N):
    best = max(best, energy(i, M - 1, 2))

print(best)
