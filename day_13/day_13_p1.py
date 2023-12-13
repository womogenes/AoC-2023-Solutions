with open("./day_13.in") as fin:
    patterns = [lines.split("\n")
                for lines in fin.read().strip().split("\n\n")]


def is_horiz(grid, i):
    n, m = len(grid), len(grid[0])
    # Vertical line of reflection
    for j in range(m):
        for k1 in range(n):
            k2 = i*2+1 - k1
            if not (0 <= k2 < n):
                continue
            if grid[k1][j] != grid[k2][j]:
                return False

    return True


def transpose(grid):
    return list(zip(*grid))


def summary(grid):
    n, m = len(grid), len(grid[0])

    horiz = -1
    for i in range(n-1):
        if is_horiz(grid, i):
            horiz = i
            break

    vert = -1
    T = transpose(grid)
    for j in range(m-1):
        if is_horiz(T, j):
            vert = j
            break

    assert vert == -1 or horiz == -1
    return vert + 1 + 100 * (horiz + 1)


ans = 0
for grid in patterns:
    summ = summary(grid)
    ans += summ

print(ans)
