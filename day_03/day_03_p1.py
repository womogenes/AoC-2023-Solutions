with open("day_03.in") as fin:
    data = fin.read()
    lines = data.strip().split("\n")

n = len(lines)
m = len(lines[0])


def is_symbol(i, j):
    if not (0 <= i < n and 0 <= j < m):
        return False

    return lines[i][j] != "." and not lines[i][j].isdigit()


ans = 0

for i, line in enumerate(lines):
    start = 0

    j = 0

    while j < m:
        start = j
        num = ""
        while j < m and line[j].isdigit():
            num += line[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)

        # Number ended, look around
        if is_symbol(i, start-1) or is_symbol(i, j):
            ans += num
            continue

        for k in range(start-1, j+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                ans += num
                break

print(ans)
