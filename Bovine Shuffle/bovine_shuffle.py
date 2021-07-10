with open('bovine_shuffle.in', 'r') as file:
    number, line, line2 = int(file.readline().strip()), list(map(int, file.readline().strip().split())), list(map(int, file.readline().strip().split()))

a = [[value, line2[index]] for index, value in enumerate(line)]
org, z = [each[0] for each in a], [each[1] for each in a]

b = [z[org[index]-1] for index, value in enumerate(z)]
c = [b[org[index]-1] for index, value in enumerate(b)]
d = [c[org[index]-1] for index, value in enumerate(c)]

print(b,c,d)

with open('bovine_shuffle.out', 'w') as file2:
    for each in d: print(str(each), file=file2)
