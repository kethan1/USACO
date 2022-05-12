import math

sections_traffic = []

with open("traffic.in") as input_file:
    sections = int(input_file.readline())
    for line in input_file:
        line = line.strip().split()
        sections_traffic.append([line[0], int(line[1]), int(line[2])])

total_traffic_min = -math.inf
total_traffic_max = math.inf

for traffic in sections_traffic:
    if traffic[0] == "on":
        total_traffic_min += traffic[1]
        total_traffic_max += traffic[2]
    elif traffic[0] == "off":
        total_traffic_min -= traffic[2]
        total_traffic_max -= traffic[1]
    else:
        total_traffic_min = max(total_traffic_min, traffic[1])
        total_traffic_max = min(total_traffic_max, traffic[2])

starting_traffic_min = -math.inf
starting_traffic_max = math.inf

for traffic in reversed(sections_traffic):
    if traffic[0] == "on":
        starting_traffic_min -= traffic[2]
        starting_traffic_max -= traffic[1]
    elif traffic[0] == "off":
        starting_traffic_min += traffic[1]
        starting_traffic_max += traffic[2]
    else:
        starting_traffic_min = max(starting_traffic_min, traffic[1])
        starting_traffic_max = min(starting_traffic_max, traffic[2])

with open("traffic.out", "w") as output_file:
    print(
        max(0, starting_traffic_min),
        max(0, starting_traffic_max),
        file=output_file,
    )
    print(max(total_traffic_min, 0), max(total_traffic_max, 0), file=output_file)
