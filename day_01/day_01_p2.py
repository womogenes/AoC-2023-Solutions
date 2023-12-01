with open("day_01.in") as fin:
    data = fin.read()

ans = 0
nums = ["one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"]

for line in data.strip().split():
    first = None
    last = None

    for i in range(len(line)):
        cur = None

        c = line[i]
        if c.isdigit():
            cur = int(c)

        for j, num in enumerate(nums):
            if line[i:(i+len(num))] == num:
                cur = j + 1
                break

        if cur:
            if first == None:
                first = cur
            last = cur

    ans += first * 10 + last


print(ans)
