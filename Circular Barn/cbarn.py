import math

with open("cbarn.in") as input_file:
    N = int(input_file.readline())
    rooms = list(map(int, input_file.readlines()))

min_distance = math.inf
for index, _ in enumerate(rooms):
    offset = rooms[index:] + rooms[:index]
    offset = [num * index for index, num in enumerate(offset)]
    min_distance = min(min_distance, sum(offset))

with open("cbarn.out", "w") as output_file:
    print(min_distance, file=output_file)
