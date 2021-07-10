with open("even_more_odd_photos.in") as input_file:
    N = int(input_file.readline().strip())
    breed_IDs = list(map(int, input_file.readline().strip().split()))

odds = 0
evens = 0
for i in breed_IDs:
    if i%2 == 0:
        evens+=1
    else:
        odds+=1

groups = 0
if odds == 0:
    groups = 1
elif evens == 0:
    x = []
    for i in breed_IDs:
        x.append
    groups = len(breed_IDs)-(len(breed_IDs)/3)
elif odds == evens:
    groups = N
elif odds+1 == evens:
    groups = N
print(groups)
