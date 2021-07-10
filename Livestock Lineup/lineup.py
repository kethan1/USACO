file = open("lineup.in", "r")
numofr = file.readline().strip()
lines = []
cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
for line in file:
    lines.append(line.strip().split(" ")[0]+" "+line.strip().split()[-1])

file.close()

file2 = open("lineup.out", "w")

found = 0
order = []
ins = []
used = []

# for thing in cows:
#     for thing2 in lines:
#         if thing in thing2.split():
#             found+=1
#             ins.append(order.append(thing2.split()[0]))
#             if found == 2:
#                 order.append(thing2.split()[0])
#                 order.append(thing2.split()[1])
#                 order.append(ins[0])
#                 used.append(order.append(thing2.split()[0]))
#                 used.append(order.append(thing2.split()[1]))
#                 used.append(ins[0])
#         found = 0
#         ins = []
#                
# for thing3 in cows:
#     if thing3 not in used:
#         order.append(thing3)

cows.sort()

for thing in lines:
    list1 = thing.split()
    try:
        if next(iter(cows[1::])) != list1[0]:
            cows.remove(next(iter(list1[8::])))
#             cows.append(list1[1])
    except:
        pass

print(cows)

file2.close()
