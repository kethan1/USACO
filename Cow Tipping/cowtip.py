with open("cowtip.in") as cowtip_input:
    cowtip_input.readline()
    cows = [[*map(int, list(line.strip()))] for line in cowtip_input]


def cow_tipper(pos2_x, pos2_y, cowsList):
    for index in range(0, pos2_x + 1):
        for index2 in range(0, pos2_y + 1):
            cowsList[index][index2] = 1 - cowsList[index][index2]  # flips the cow (converts 1 to 0 and 0 to 1)


cow_tippers_used = 0
for index in range(len(cows) - 1, -1, -1):
    for index2 in range(len(cows[index]) - 1, -1, -1):
        if cows[index][index2]:
            cow_tipper(index, index2, cows)
            cow_tippers_used += 1

with open("cowtip.out", "w") as cowtip_output:
    cowtip_output.write(str(cow_tippers_used))
