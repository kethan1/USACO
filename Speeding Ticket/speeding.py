with open("speeding.in") as input_file:
    N, M = map(int, input_file.readline().split())
    speed_limits = [list(map(int, input_file.readline().split())) for _ in range(N)]
    bessie = [list(map(int, line.split())) for line in input_file]
    print(N, M, speed_limits, bessie)

speed_limits_total = [speed for distance, speed in speed_limits for _ in range(distance)]
bessie_total = [speed for distance, speed in bessie for _ in range(distance)]

max_speed_above_limit = 0

for index, speed in enumerate(bessie_total):
    max_speed_above_limit = max(max_speed_above_limit, bessie_total[index] - speed_limits_total[index])

with open("speeding.out", "w") as output_file:
    output_file.write(str(max_speed_above_limit))
