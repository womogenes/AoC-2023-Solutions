with open("day_02.in") as fin:
    data = fin.read().strip().split("\n")

ans = 0

for line in data:
    game, parts = line.split(": ")
    _id = int(game.split(" ")[1])

    good = True
    for part in parts.split("; "):
        for cubes in part.split(", "):
            num, color = cubes.split(" ")
            num = int(num)

            if color == "red" and num > 12:
                good = False
            if color == "blue" and num > 14:
                good = False
            if color == "green" and num > 13:
                good = False

            if not good:
                break

        if not good:
            break

    if good:
        ans += _id

print(ans)
