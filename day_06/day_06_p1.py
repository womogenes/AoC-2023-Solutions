with open("./day_06.in") as fin:
    lines = fin.read().strip().split()

times = [45, 97, 72, 95]
dists = [305, 1062, 1110, 1695]


def ways(t, d):
    count = 0
    for i in range(t):
        # Hold down for i seconds
        if (t - i) * i > d:
            count += 1

    return count


ans = []
for t, d in zip(times, dists):
    ans.append(ways(t, d))

p = 1
for x in ans:
    p *= x

print(p)
