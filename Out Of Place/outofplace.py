with open("outofplace.in") as input_file:
    input_file.readline()
    cows = [int(line) for line in input_file]

swaps = -1
for index, cow in enumerate(sorted(cows)):
    if cows[index] != cow:
        swaps += 1

with open("outofplace.out", "w") as output_file:
    output_file.write(str(swaps))
