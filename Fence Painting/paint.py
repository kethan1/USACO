file1 = open("paint.in", "r")

line1 = file1.readline()
line2 = file1.readline()

a, b = int(line1.split()[0]), int(line1.split()[1])
c, d = int(line2.split()[0]), int(line2.split()[1])

file1.close()

lst = [*range(1, max(a, b, c, d))]
lenlst = len(lst)

for thing in range(a, b):
    if thing in lst:
        lst.remove(thing)

for thing in range(c, d+1):
    if thing in lst:
        lst.remove(thing)

with open("paint.out", "w") as output_file:
    print(lenlst-len(lst), file=output_file)
