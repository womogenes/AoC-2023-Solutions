with open("./day_15.in") as fin:
    line = fin.read().strip()


def HASH(s):
    cur = 0
    for c in s:
        cur += ord(c)
        cur *= 17
        cur %= 256
    return cur


parts = line.split(",")
cur = 0
ans = 0
for part in parts:
    cur = HASH(part)
    ans += cur

print(ans)
