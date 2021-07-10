with open("cowtip.in") as cowtip_input:
    N = int(cowtip_input.readline())
    cows = [list(map(int, list(line.strip()))) for line in cowtip_input]

def cow_tipper(pos1, pos2):
    for index in range(pos1[0], pos2[0]+1):
        for index2 in range(pos1[1], pos2[1]+1):
            cows[index][index2] = int(not bool(cows[index][index2]))

cows_length = len(cows)-1
cow_tippers_used = 0
for index in range(cows_length, -1, -1):
    cows_sublist_length = len(cows[index])-1
    for index2 in range(cows_sublist_length, -1, -1):
        if cows[index][index2] == 1:
            cow_tipper((0,0), (index, index2))
            cow_tippers_used+=1

with open("cowtip.out", "w") as cowtip_output:
    print(cow_tippers_used, file=cowtip_output)
