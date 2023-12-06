with open("./day_06.in") as fin:
    lines = fin.read().strip().split("\n")


t = int("".join(lines[0].split()[1:]))
d = int("".join(lines[1].split()[1:]))


def ways(t, d):
    count = 0
    for i in range(t):
        # Hold down for i seconds
        if (t - i) * i > d:
            count += 1

    return count


print(ways(t, d))
