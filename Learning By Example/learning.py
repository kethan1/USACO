# Broken, doesn't pass test cases

import math

with open("learning.in") as input_file:
    N, A, B = map(int, input_file.readline().split())
    cows = []
    for cow in input_file:
        spotted, weight = cow.split()
        cows.append([spotted, int(weight)])

cows.sort(key=lambda x: x[1])
print(cows)
print(N, A, B)
spotted = 0
area_covered = {}
for index, cow in enumerate(cows):
    if index == len(cows) - 1:
        area_covered[index] = [area_covered[index-1][1], B]
        if cow[0] == "S":
            if B - area_covered[index][0] > 0:
                spotted += (B - area_covered[index][0])
        print(index, cow, area_covered[index][1] - area_covered[index][0])
    else:
        end_point = (cows[index+1][1] + cow[1]) / 2
        if index == 0:
            if cow[0] == "S":
                area_covered[index] = [A, math.ceil(end_point)]
            else:
                area_covered[index] = [A, math.floor(end_point)]
        else:
            if cow[0] == "S":
                area_covered[index] = [area_covered[index-1][1], math.ceil(end_point)]
            else:
                area_covered[index] = [area_covered[index-1][1], math.floor(end_point)]
        if cow[0] == "S":
            if area_covered[index][1] - area_covered[index][0] < 0:
                print(index, cow)
            if index != 0 and (area_covered[index][1] - area_covered[index][0]) != 0:
                spotted += (area_covered[index][1] - area_covered[index][0])
            else:
                spotted += area_covered[index][1] - area_covered[index][0]
        print(index, cow, area_covered[index][1] - area_covered[index][0])
# print(area_covered)

# print(area_covered)

print(spotted)

with open("learning.out", "w") as output_file:
    output_file.write(str(spotted))
