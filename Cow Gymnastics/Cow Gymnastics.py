file = open("Cow Gymnastics.in", "r")

line1 = file.readline().strip().split()
print(line1)
lines = []

for line in file:
    line = line.strip()
    lines.append(line)
    
print(lines)

file.close()



for thing in lines:
    if thing[0] > thing[2]:
        