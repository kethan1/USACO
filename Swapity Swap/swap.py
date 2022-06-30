with open("swap.in") as input_file:
    N, K = map(int, input_file.readline().split())
    a1, a2 = map(int, input_file.readline().split())
    b1, b2 = map(int, input_file.readline().split())

cows = list(range(1, N + 1))
cows_copy = cows.copy()
cows_copy[a1 - 1: a2] = reversed(cows_copy[a1 - 1: a2])
cows_copy[b1 - 1: b2] = reversed(cows_copy[b1 - 1: b2])
repeat_period = 1
while cows != cows_copy:
    cows_copy[a1 - 1: a2] = reversed(cows_copy[a1 - 1: a2])
    cows_copy[b1 - 1: b2] = reversed(cows_copy[b1 - 1: b2])
    repeat_period += 1

for _ in range(K % repeat_period):
    cows[a1 - 1: a2] = reversed(cows[a1 - 1: a2])
    cows[b1 - 1: b2] = reversed(cows[b1 - 1: b2])

with open("swap.out", "w") as output_file:
    print("\n".join(map(str, cows)), file=output_file)
