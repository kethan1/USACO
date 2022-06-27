with open("revegetate.in", "r") as input_file:
    N, M = list(map(int, input_file.readline().strip().split()))
    fields = list(range(1, N + 1))
    adjacency_list = {field: [] for field in fields}
    for line in input_file:
        a, b = list(map(int, line.strip().split()))
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

crops_planted = {field: -1 for field in fields}
crops_planted[1] = 1
options = {1, 2, 3, 4}
for field in fields[1:]:
    taken = {crops_planted[adjacent_field] for adjacent_field in adjacency_list[field]}
    new_options = options - taken
    crops_planted[field] = min(new_options)

with open("revegetate.out", "w") as output_file:
    print("".join(map(str, crops_planted.values())), file=output_file)
