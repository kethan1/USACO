with open("blist.in", "r") as input_file:
    input_file.readline()
    cows = []
    for line in input_file.readlines():
        line = line.strip().split()
        for num in line:
            line[line.index(num)] = int(num)
        cows.append(line)

buckets = sum([cow[2] for cow in cows])
buckets_in_list = {key: (False, False) for key in range(buckets)}

cows.sort(key=lambda x: x[0])

returns = {cow[1]: cow[2] for cow in cows}

time = 0
buckets_used = 0
for cow in cows:
    while time != cow[0]:
        go = True
        for key, value in returns.items():
            if go:
                if key == time:
                    returned = 0
                    for key1, value1 in buckets_in_list.items():
                        if go:
                            if value1[1]:
                                buckets_in_list[key1] = (value1[0], False)
                                returned += 1
                                if returned == value:
                                    go = False
                        else:
                            break
            else:
                break
        time += 1
    a = 0
    for key, value in buckets_in_list.items():
        if value[0]:
            if not value[1]:
                a += 1
                buckets_in_list[key] = (True, True)
            if a == cow[2]:
                break
    if a == cow[2]:
        pass
    else:
        needed = cow[2]-a
        fullfilled = 0
        for key, value in buckets_in_list.items():
            if fullfilled < needed:
                if not any(value):
                    buckets_in_list[key] = (True, True)
                    buckets_used += 1
                    fullfilled += 1
            else:
                break

with open("blist.out", "w") as output_file:
    print(buckets_used, file=output_file)
