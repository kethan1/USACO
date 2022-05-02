import itertools
import math

with open("pails.in") as input_file:
    X, Y, M = map(int, input_file.readline().strip().split())

closest_distance = math.inf

for num_of_x_fills, num_of_y_fills in itertools.product(range(M), range(M)):
    dif = M - (X * num_of_x_fills + Y * num_of_y_fills)
    if dif < 0:
        continue
    closest_distance = min(closest_distance, dif)

with open("pails.out", "w") as output_file:
    print(int(M - closest_distance), file=output_file)
