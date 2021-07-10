# N = int(input())
# flowers = list(map(int, input().split()))

with open("daisy_chains.in", "r") as file:
    N = int(file.readline())
    flowers = list(map(int, file.readline().strip().split()))
flower_pairs = [[flowers[i], flowers[i]] for i in range(len(flowers))]
for x in range(0, len(flowers)-1):
    for y in range(x+1, len(flowers)):
        z = []
        for i in range(x, y+1): z.append(flowers[i])
        flower_pairs.append(z)
average_flowers = 0
for i in flower_pairs: 
    if sum(i)/len(i) in i: average_flowers+=1

print(average_flowers)
