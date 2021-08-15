# Not working

import itertools

with open('lifeguards.in') as input_file:
    N = int(input_file.readline())
    lifeguards = [[*map(int, line.split())] for line in input_file]

print(lifeguards)

lifeguard_combinations = itertools.combinations(lifeguards, len(lifeguards) - 1)
lifeguard_combinations = [lifeguards]

max_time_covered = 0

for lifeguard_combination in lifeguard_combinations:
    time = 0
    for index, guard in enumerate(lifeguard_combination):
        time += guard[1] - guard[0]
        subtracted_times = []
        for guard_dupe in lifeguard_combination[:index]:
            if guard_dupe != guard:
                # print(guard, guard_dupe)
                if guard_dupe[0] <= guard[0] <= guard_dupe[1]:
                    # print(guard, guard_dupe)
                    if guard == [4, 5]:
                        print(guard, guard_dupe)
                    subtracted_times.append([guard_dupe[1], guard[0]])
                    time -= (guard_dupe[1] - guard[0]) + 1

                if guard_dupe[0] <= guard[1] <= guard_dupe[1]:
                    print(guard, guard_dupe)
                    subtracted_times.append([guard[1], guard_dupe[0]])
                    time -= guard[1] - guard_dupe[0]

    max_time_covered = max(max_time_covered, time)

print(time)

# answer = 0
# ranges = []
# for combination in combinations:
#     for combination2 in combinations:
#         if combination != combination2:
#             pass

with open('lifeguards.out', 'w') as output_file:
    output_file.write(str(max_time_covered))
