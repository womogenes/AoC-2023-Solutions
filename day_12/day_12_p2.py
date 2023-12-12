from tqdm import tqdm
from pprint import pprint

with open("./day_12.in") as fin:
    lines = fin.read().strip().split("\n")

ss = []
target_runs = []
for line in lines:
    parts = line.split(" ")
    parts[0] = "?".join([parts[0]] * 5)
    parts[1] = ",".join([parts[1]] * 5)

    ss.append(parts[0])
    target_runs.append(list(map(int, parts[1].split(","))))


def ways(s, target_runs):
    # This is what I get for not investing in DP (dyanmic programming)
    # 3D dp on (idx in string, idx in set, length of current run)
    # Question: How many ways?
    target_runs.append(0)
    max_run = max(target_runs)
    s += "."

    n = len(s)
    m = len(target_runs)
    dp = [[[None for _ in range(max_run+1)]
           for _ in range(m)] for _ in range(n)]

    for i in range(n):
        x = s[i]
        for j in range(m):
            for k in range(target_runs[j]+1):
                # Base case
                if i == 0:
                    if j != 0:
                        dp[i][j][k] = 0
                        continue

                    if x == "#":
                        if k != 1:
                            dp[i][j][k] = 0
                            continue
                        dp[i][j][k] = 1
                        continue

                    if x == ".":
                        if k != 0:
                            dp[i][j][k] = 0
                            continue
                        dp[i][j][k] = 1
                        continue

                    if x == "?":
                        if k not in [0, 1]:
                            dp[i][j][k] = 0
                            continue
                        dp[i][j][k] = 1
                        continue

                # Process answer if current char is .
                if k != 0:
                    ans_dot = 0
                elif j > 0:
                    assert k == 0
                    ans_dot = dp[i-1][j-1][target_runs[j-1]]
                    ans_dot += dp[i-1][j][0]
                else:
                    # i>0, j=0, k=0.
                    # Only way to do this is if every ? is a .
                    ans_dot = 1 if s[:i].count("#") == 0 else 0

                # Process answer if current char is #
                if k == 0:
                    ans_pound = 0
                else:
                    # Newest set
                    ans_pound = dp[i-1][j][k-1]

                if x == ".":
                    dp[i][j][k] = ans_dot
                elif x == "#":
                    dp[i][j][k] = ans_pound
                else:
                    dp[i][j][k] = ans_dot + ans_pound

    ans = dp[n-1][-1][0]

    return ans


ans = 0
for s, target_run in tqdm(list(zip(ss, target_runs)), ncols=70):
    res = ways(s, target_run)
    ans += res

print(ans)
