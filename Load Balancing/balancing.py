import math


with open("balancing.in") as input_file:
    N, B = map(int, input_file.readline().split())
    cows = [tuple(map(int, line.split())) for line in input_file]

min_maximum_cows = math.inf
for x_index in range(N):
    for y_index in range(N):
        a, _ = cows[x_index]
        _, b = cows[y_index]
        q1 = q2 = q3 = q4 = 0  # Follows coordinate plane quadrant numbering
        for cow in cows:
            x, y = cow
            if x < a:
                if y < b:
                    q3 += 1
                else:
                    q2 += 1
            else:
                if y < b:
                    q4 += 1
                else:
                    q1 += 1
        min_maximum_cows = min(min_maximum_cows, max(q1, q2, q3, q4))

with open("balancing.out", "w") as output_file:
    print(min_maximum_cows, file=output_file)
