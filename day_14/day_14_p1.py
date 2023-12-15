with open("./day_14.in") as fin:
    lines = fin.read().strip().split("\n")

n, m = len(lines), len(lines[0])

# Tilt all the rocks up


def process_col(j):
    # Process column j
    i = 0
    ans = 0

    print(f"=== Column {j} ===")

    while i < n:
        while i < n and lines[i][j] == "#":
            i += 1

        # Now we're at an O or a .
        count = 0
        start = i
        while i < n and lines[i][j] != "#":
            if lines[i][j] == "O":
                count += 1
            i += 1

        print(f"  Range from {start} to {i}, count={count}")

        for ii in range(start, start + count):
            ans += n - ii

    return ans


ans = 0
for j in range(m):
    ans += process_col(j)

print(ans)
