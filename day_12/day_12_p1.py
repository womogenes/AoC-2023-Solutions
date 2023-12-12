from tqdm import tqdm

with open("./day_12.in") as fin:
    lines = fin.read().strip().split("\n")

ss = []
target_runs = []
for line in lines:
    parts = line.split(" ")
    ss.append(parts[0])
    target_runs.append(list(map(int, parts[1].split(","))))


def valid(line, target_runs):
    n = len(line)
    runs = []

    i = 0
    while i < n:
        while i < n and not line[i]:
            i += 1
        if i == n:
            break
        j = i
        c = 0
        while j < n and line[j]:
            j += 1
            c += 1

        runs.append(c)
        i = j

    return runs == target_runs


def ways(s, target_runs):
    line = []
    idxs = []
    for i, x in enumerate(s):
        if x == ".":
            line.append(0)
        if x == "?":
            line.append(-1)
            idxs.append(i)
        if x == "#":
            line.append(1)

    count = 0
    for mask in range(1 << len(idxs)):
        line_copy = line.copy()
        for i in range(len(idxs)):
            if mask & (1 << i):
                line_copy[idxs[i]] = 0
            else:
                line_copy[idxs[i]] = 1

        if valid(line_copy, target_runs):
            count += 1

    return count


ans = 0
for s, target_run in tqdm(list(zip(ss, target_runs))):
    res = ways(s, target_run)
    ans += res

print(ans)
