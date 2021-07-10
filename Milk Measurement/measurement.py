file = open("measurement.in")
lines = file.readline()
log = []
for line in file:
    day, cow, change = line.strip().split()
    log.append([int(day),cow,int(change)])

log.sort(key=lambda x: x[0])

changes = 0
dict1 = {"Bessie": 7, "Elsie": 7, "Mildred": 7}

for thing in log:
    dict2 = dict1.copy()
    dict2[thing[1]] += thing[2]
    if (list(dict1.keys())[list(dict1.values()).index(max(dict1.values()))]) != (list(dict2.keys())[list(dict2.values()).index(max(dict2.values()))]):
        changes += 1
    if list(dict1.values()).count(max(dict1.values())) != list(dict2.values()).count(max(dict1.values())):
        changes += 1
    dict1 = dict2

with open("measurement.out", "w") as output_file:
    output_file.write(str(changes))
