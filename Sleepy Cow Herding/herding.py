with open("herding.in") as input_file:
    a, b, c = list(map(int, input_file.readline().split()))

min_moves = 0 if a + 2 == c else 1 if b == a + 2 or c == b + 2 else 2
max_moves = max(b-a, c-b) - 1

with open("herding.out", "w") as output_file:
    print(min_moves, file=output_file)
    print(max_moves, file=output_file)
