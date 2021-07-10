with open("cowroute.in", "r") as file1:    
    A, B, N = map(int, file1.readline().strip().split(" "))
    routes = [[list(map(int, file1.readline().strip().split(" "))), list(map(int, file1.readline().strip().split(" ")))] for _ in range(N)]
intermediate_cities = []
for city in [route[0] for route in routes]:
    for each_city in city:
        cost1, cost2 = [], []
        for route in routes:
            if (A in route[1] and each_city in route[1]) and (route[1].index(A) < route[1].index(each_city)): cost1.append(route[0][0])
            if (each_city in route[1] and B in route[1]) and (route[1].index(each_city) < route[1].index(B)): cost2.append(route[0][0])
        if [] not in (cost1, cost2): intermediate_cities.append(min(cost1)+min(cost2))
z = [route[0][0] for route in routes if A in route[1] and B in route[1] if route[1].index(A) < route[1].index(B)]
if z != []: intermediate_cities.append(min(z))

with open("cowroute.out", "w") as file2:
    print(min(intermediate_cities), file=file2)