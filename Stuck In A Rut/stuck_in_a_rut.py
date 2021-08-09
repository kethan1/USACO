# Testing

with open("stuck_in_a_rut.in") as file1:
    N = int(file1.readline().strip())
    cows = [[value if index == 0 else int(value) for index, value in enumerate(i.strip().split())] for i in file1.readlines()]


# Actual
# N = int(input())
# cow_numbers = [input() for _ in range(N)]
# cows = [[value if index == 0 else int(value) for index, value in enumerate(i.strip().split())] for i in cow_numbers]

future_path = {}
max_x, max_y = max(cows, key=lambda x: x[1])[1], max(cows, key=lambda x: x[2])[2]
for i in range(1, N+1):
    tmp_lst = [[1, cows[i-1][1], cows[i-1][2]]]
    if cows[i-1][0] == "E":
        tmp_1 = 2
        for x in range(cows[i-1][1]+1, max_x+1):
            tmp_lst.append([tmp_1, x, cows[i-1][2]])
            tmp_1 += 1
    elif cows[i-1][0] == "N":
        tmp_1 = 2
        for x in range(cows[i-1][2]+1, max_x+1):
            tmp_lst.append([tmp_1, cows[i-1][1], x])
            tmp_1 += 1
    future_path[i] = tmp_lst
future_path_list = [x for key, value in future_path.items() for x in value]

for key, value in future_path.items():
    print(key, ": ", value, sep="")
finish = {i: None for i in range(1, N+1)}
for key, value in future_path.items():
    x = True
    number_eaten = 0
    for i in value:
        for y in future_path_list:
            if i[1:] == y[1:]:
                if i[0] > y[0]:
                    n = True
                    for g in future_path_list:
                        if y[1:] == g[1:]:
                            if y == [5, 11, 6]:
                                print("**********************************")
                                print(y, g)
                                print("**********************************")
                            if y[0] > g[0]:
                                n = False
                    print(i, y, key)
                    if n:
                        x = False
        if x:
            number_eaten += 1
    finish[key] = [number_eaten, x]
print(finish)
