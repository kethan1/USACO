with open("mixmilk.in", "r") as input_file:
    bucket1 = list(map(int, input_file.readline().split()))
    bucket2 = list(map(int, input_file.readline().split()))
    bucket3 = list(map(int, input_file.readline().split()))
    print(bucket1, bucket2, bucket3)

# 0 for bucket1 to bucket2, 1 for bucket2 to bucket3, 2 for bucket1 to bucket3
spot = 0
for _ in range(100):
    if spot == 0:
        # Move bucket1 to bucket2
        if bucket1[1] + bucket2[1] <= bucket2[0]:
            bucket2[1] += bucket1[1]
            bucket1[1] = 0
        else:
            capacity_left = bucket2[0] - bucket2[1]
            bucket2[1] = bucket2[0]
            bucket1[1] -= capacity_left
        spot = 1

    elif spot == 1:
        # Move bucket2 to bucket3
        if bucket2[1] + bucket3[1] <= bucket3[0]:
            bucket3[1] += bucket2[1]
            bucket2[1] = 0
        else:
            capacity_left = bucket3[0] - bucket3[1]
            bucket3[1] = bucket3[0]
            bucket2[1] -= capacity_left
        spot = 2

    elif spot == 2:
        # Move bucket3 to bucket1
        if bucket3[1] + bucket1[1] <= bucket1[0]:
            bucket1[1] += bucket3[1]
            bucket3[1] = 0
        else:
            capacity_left = bucket1[0] - bucket1[1]
            bucket1[1] = bucket1[0]
            bucket3[1] -= capacity_left
        spot = 0

with open('mixmilk.out', 'w') as output_file:
    output_file.write(f'{bucket1[1]}\n{bucket2[1]}\n{bucket3[1]}')
