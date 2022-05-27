import itertools

with open("gymnastics.in") as input_file:
    K, N = map(int, input_file.readline().split())
    weeks = [list(map(int, line.split())) for line in input_file]

pairs = 0
for combination in itertools.permutations(weeks[0], 2):
    consistent = all(week.index(combination[0]) >= week.index(combination[1]) for week in weeks)

    pairs += consistent

with open("gymnastics.out", "w") as output_file:
    print(pairs, file=output_file)
