from copy import deepcopy
from tqdm import tqdm
from pprint import pprint

with open("./day_14.in") as fin:
    lines = [list(line) for line in fin.read().strip().split("\n")]

n, m = len(lines), len(lines[0])

# North, west, south, east


def north_load(grid):
    n, m = len(grid), len(grid[0])

    # Process column j
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "O":
                ans += n - i
    return ans


def tilt_up(grid):
    n, m = len(grid), len(grid[0])

    # Process column j
    for j in range(m):
        i = 0
        while i < n:
            while i < n and grid[i][j] == "#":
                i += 1

            # Now we're at an O or a .
            count = 0
            start = i
            while i < n and grid[i][j] != "#":
                if grid[i][j] == "O":
                    count += 1
                i += 1

            for ii in range(start, start + count):
                grid[ii][j] = "O"
            for ii in range(start + count, i):
                grid[ii][j] = "."

    return grid


def rotate_90(grid):
    # Rotate by 90 deg counterclockwise
    new_grid = [[None] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_grid[i][j] = grid[j][m-1-i]
    return new_grid


def rotate(grid, i):
    # Rotate grid by i*90 deg counterclockwise
    grid_copy = deepcopy(grid)
    for _ in range(i % 4):
        grid_copy = rotate_90(grid_copy)
    return grid_copy


cycle2grid = {}
seen = {}


def get_hash(grid):
    return "\n".join(["".join(line) for line in grid])


def do_cycle(grid):
    grid_copy = deepcopy(grid)
    for i in range(4):
        grid_copy = rotate(grid_copy, 4 - (i % 4))
        grid_copy = tilt_up(grid_copy)
        grid_copy = rotate(grid_copy, i % 4)
    return grid_copy


grid = lines
for cycle in range(10**9):
    grid = do_cycle(grid)

    h = get_hash(grid)
    if h in seen:
        period = cycle - seen[h]
        ans_grid = cycle2grid[(10**9 - 1 - seen[h]) % period + seen[h]]
        print(north_load(ans_grid))
        break

    seen[get_hash(grid)] = cycle
    cycle2grid[cycle] = deepcopy(grid)
