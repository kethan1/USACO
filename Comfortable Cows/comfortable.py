N = int(input())
cows = set()
cow_comfort = {}

comfortable = 0

for _ in range(N):
    cow = tuple(map(int, input().split()))
    cows.add(cow)
    cow_comfort[cow] = 0

    x, y = cow

    if (x + 1, y) in cows:
        cow_comfort[(x + 1, y)] += 1
        cow_comfort[cow] += 1

        if cow_comfort[(x + 1, y)] == 3:
            comfortable += 1
        elif cow_comfort[(x + 1, y)] == 4:
            comfortable -= 1

    if (x - 1, y) in cows:
        cow_comfort[(x - 1, y)] += 1
        cow_comfort[cow] += 1

        if cow_comfort[(x - 1, y)] == 3:
            comfortable += 1
        elif cow_comfort[(x - 1, y)] == 4:
            comfortable -= 1

    if (x, y + 1) in cows:
        cow_comfort[(x, y + 1)] += 1
        cow_comfort[cow] += 1

        if cow_comfort[(x, y + 1)] == 3:
            comfortable += 1
        elif cow_comfort[(x, y + 1)] == 4:
            comfortable -= 1

    if (x, y - 1) in cows:
        cow_comfort[(x, y - 1)] += 1
        cow_comfort[cow] += 1

        if cow_comfort[(x, y - 1)] == 3:
            comfortable += 1
        elif cow_comfort[(x, y - 1)] == 4:
            comfortable -= 1

    if cow_comfort[cow] == 3:
        comfortable += 1

    print(comfortable)
