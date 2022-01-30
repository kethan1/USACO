with open("photo.in") as input_file:
    N = int(input_file.readline())
    b = list(map(int, input_file.readline().split()))

possibilites = []
for a0 in range(1, b[0]):
    if b[0] - a0 != a0:
        permutations = [a0, b[0] - a0]
        stop = False
        for number in b[1:]:
            new_number = number - permutations[-1]
            if new_number in permutations or new_number <= 0:
                stop = True
                break
            permutations.append(new_number)
        if not stop:
            possibilites.append(permutations)


def all_equal(iterator):
    return all(iterator[0] == x for x in iterator)


columns = [
    [possibility[index] for possibility in possibilites]
    for index in range(len(possibilites[0]))
]
min_index = 0
for column in columns:
    if not all_equal(column):
        min_index = column.index(min(column))
with open("photo.out", "w") as output_file:
    print(*possibilites[min_index], file=output_file)
