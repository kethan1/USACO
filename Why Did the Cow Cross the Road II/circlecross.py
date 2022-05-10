with open("circlecross.in") as input_file:
    crossings = input_file.readline().strip()

pasture_cows = {}
crosses = 0
for index, crossing in enumerate(crossings):
    if crossing not in pasture_cows:
        pasture_cows[crossing] = index
    else:
        for cow in pasture_cows:
            if cow != crossing and pasture_cows[crossing] < pasture_cows[cow]:
                crosses += 1
        del pasture_cows[crossing]

with open("circlecross.out", "w") as output_file:
    print(crosses, file=output_file)
