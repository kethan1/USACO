import itertools

with open("guess.in") as input_file:
    input_file.readline()
    characteristics = [animal.strip().split()[2:] for animal in input_file]

most_shared = 0
for animal1, animal2 in itertools.combinations(characteristics, 2):
    most_shared = max(len(set(animal1).intersection(animal2)), most_shared)

with open("guess.out", "w") as output_file:
    output_file.write(str(most_shared + 1))
