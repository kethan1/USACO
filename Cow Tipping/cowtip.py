with open("cowtip.in") as cowtip_input:
    cowtip_input.readline()
    cows = [list(map(int, list(line))) for line in cowtip_input]


def cow_tipper(pos1_x, pos1_y, pos2_x, pos2_y, cowsList):
    for index in range(pos1_x, pos2_x + 1):
        for index2 in range(pos1_y, pos2_y + 1):
            cowsList[index][index2] = 1 - cowsList[index][index2]


cow_tippers_used = 0
for index in range(len(cows) - 1, -1, -1):
    for index2 in range(len(cows[index]) - 1, -1, -1):
        if cows[index][index2] == 1:
            cow_tipper(0, 0, index, index2, cows)
            cow_tippers_used += 1

with open("cowtip.out", "w") as cowtip_output:
    cowtip_output.write(str(cow_tippers_used))
