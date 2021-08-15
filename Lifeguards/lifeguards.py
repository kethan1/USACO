import itertools

with open('lifeguards.in') as input_file:
    input_file.readline()
    lifeguards = [[*map(int, line.split())] for line in input_file]

lifeguard_combinations = itertools.combinations(lifeguards, len(lifeguards) - 1)

max_time_covered = 0

for lifeguard_combination in lifeguard_combinations:
    time_covered = 0
    for time in range(min(map(min, lifeguards)), max(map(max, lifeguards)) + 1):
        for lifeguard in lifeguard_combination:
            if lifeguard[0] <= time < lifeguard[1]:
                time_covered += 1
                break
    max_time_covered = max(max_time_covered, time_covered)

with open('lifeguards.out', 'w') as output_file:
    output_file.write(str(max_time_covered))
