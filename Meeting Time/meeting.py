with open("meeting.in", "r") as inputFile:
    numberOfFields, numberOfPaths = map(int, list(inputFile.readline().strip().split()))
    paths = [list(map(int, line.strip().split())) for line in inputFile.readlines()]

bessiepassable, elsiepassable = {str(i[0])+str(i[1]):i[2] for i in paths}, {str(i[0])+str(i[1]):i[3] for i in paths}

def remove_dups(strvar): return "".join(sorted(list(set(strvar))))

def lenofpath(strvar, dictvar):
    distance = 0
    for n in range(0, len(strvar)-1): distance = distance + dictvar[strvar[n]+strvar[n+1]]
    return distance

fieldsPath = list(set([str(i[0])+str(i[1]) for i in paths]))

first = [i for i in fieldsPath if i[0] == "1"]
second = [remove_dups(k+j) for k in first for j in fieldsPath if j[0] != "1" and k[1] == j[0]]
cowpath = [i for i in first+second if i[0] == "1" and i[-1] == str(numberOfFields)]
bessie, elsie = {}, {}

for path in cowpath:
    bessie[path], elsie[path] = lenofpath(path, bessiepassable), lenofpath(path, elsiepassable)

with open("meeting.out", "w") as outputField:
    print(min([i for x in list(elsie.values()) for i in list(bessie.values()) if i == x]), file=outputField)
