import math


with open("whereami.in") as input_file:
    N = int(input_file.readline())
    houses = input_file.readline().strip()


def window(seq, window_size):
    return [seq[i: i + window_size] for i in range(len(seq) - window_size + 1)]


min_len = math.inf
for window_size in range(1, len(houses) + 1):
    combs = window(houses, window_size)
    if len(set(combs)) == len(combs):
        min_len = min(min_len, window_size)


with open("whereami.out", "w") as output_file:
    print(min_len, file=output_file)
