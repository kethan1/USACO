file1 = open("badmilk.in", "r")
# line1 = file1.readline()
# N, M, D, S = int(line1.split()[0]), int(line1.split()[1]), int(line1.split()[2]), int(line1.split()[3])
N, M, D, S = map(int, file1.readline().split())
drankmilk = []
sickpeople = []
for thing in range(D):
    linething = file1.readline()
    drankmilk.append([int(linething.strip().split()[0]), int(linething.strip().split()[1]), int(linething.strip().split()[2])])
for line in file1.readlines():
    sickpeople.append([int(line.strip().split()[0]), int(line.strip().split()[1])])
file1.close()

sick = []
for thing in sickpeople:
    sick.append(int(thing[0]))

org = []
for thing in sick:
    org.append([thing, []])

for thing in drankmilk:
    if thing[0] in sick:
        if sickpeople[sick.index(thing[0])][1] >= thing[2]:
                for thing1 in org:
                    if thing1[0] == thing[0]:
                        thing1[1].append(thing[1])

common = org[0][1]
for thing in range(1 ,len(org)):
    thing1 = org[thing][1]
    for thing2 in common:
        if thing2 in thing1:
            pass
        else:
            common.remove(thing2)

ans = []
for thing in common:
    ans.append([])

for a in range(0, len(common)):
    for thing in drankmilk:
        if thing[1] == common[a]:
            if thing[0] not in ans[a]:
                ans[a].append(thing[0])

lens = []
for thing in ans:
    lens.append(len(thing))

file2 = open("badmilk.out", "w")
print(max(lens), file = file2)
file2.close()