with open("cowqueue.in") as input_file:
    N = int(input_file.readline())
    cows = sorted([list(map(int, line.strip().split())) for line in input_file], key=lambda a: a[0])

prev_time = 0
for cow in cows:
    if prev_time == 0 or cow[0] > prev_time:
        prev_time = cow[0] + cow[1]
    else:
        prev_time = cow[0] + (prev_time - cow[0]) + cow[1]

with open("cowqueue.out", "w") as output_file:
    print(prev_time, file=output_file)
