file = open("bucket_list.in", "r")

n = int(file.readline())
cows = []
for line in file.readlines():
    line = line.strip().split()
    for num in line:
        line[line.index(num)] = int(num)
    cows.append(line)

file.close()

buckets = 0
for cow in cows:
    buckets+=cow[2]
buckets_in_list = {}
for thing in range(buckets):
    buckets_in_list[thing] = (False, False)

cows.sort(key = lambda x: x[0])

returns = {}
for cow in cows:
    returns[cow[1]] = cow[2]

time = 0
buckets_used = 0
for cow in cows:
    while time!=cow[0]:
        go = True
        for key, value in returns.items():
            if go:
                if key == time:
                    returned = 0
                    for key1, value1 in buckets_in_list.items():
                        if go:
                            if value1[1] == True:
                                buckets_in_list[key1] = (value1[0], False)
                                returned+=1
                                if returned == value:
                                    go = False
                        else:
                            break
            else:
                break
        time+=1
    a = 0
    for key, value in buckets_in_list.items():
        if value[0]:
            if value[1] == False:
                a+=1
                buckets_in_list[key] = (True, True)
            if a == cow[2]:
                break
    if a==cow[2]:
        pass
    else:
        needed = cow[2]-a
        fullfilled = 0
        for key, value in buckets_in_list.items():
            if fullfilled < needed:
                if value[0] == False:
                    if value[1] == False:
                        buckets_in_list[key] = (True, True)
                        buckets_used+=1
                        fullfilled+=1
            else:
                break

file1 = open("bucket_list.out", "w")
print(buckets_used, file=file1)
file1.close()