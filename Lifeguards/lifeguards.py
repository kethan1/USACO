import itertools

with open('lifeguards.in') as input_file:
    N = int(input_file.readline())
    lifeguards = [[*map(int, line.strip().split())] for line in input_file]

print(lifeguards)


combinations = itertools.combinations(lifeguards, len(lifeguards) - 1)
answer = 0
ranges = []
for combination in combinations:
    for combination2 in combinations:
        if combination != combination2:
            pass

with open('lifeguards.out', 'w') as output_file:
    output_file.write(str(answer))
