# Very slow and inneficient, doesn't pass test cases

from heapq import nsmallest

with open("learning.in") as input_file:
    N, A, B = map(int, input_file.readline().split())
    cows = []
    for cow in input_file:
        spotted, weight = cow.split()
        cows.append([spotted, int(weight)])

print(cows)
print(N, A, B)
spotted = 0
for new_cow in range(A, B + 1):
    min_cow = nsmallest(2, cows, key=lambda x: abs(x[1] - new_cow))
    if min_cow[0][0] == "S":
        spotted += 1
    else:
        if min_cow[1][0] == "S":
            if abs(min_cow[0][1] - new_cow) == abs(min_cow[1][1] - new_cow):
                spotted += 1

with open("learning.out", "w") as output_file:
    output_file.write(str(spotted))
