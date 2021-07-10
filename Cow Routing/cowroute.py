with open("cowroute.in", "r") as file1:
    A, B, N = map(int, file1.readline().strip().split(" "))
    routes = [[list(map(int, file1.readline().strip().split(" "))), list(map(int, file1.readline().strip().split(" ")))] for i in range(N)]
print(routes)
costs = [route[0][0] for route in routes if A in route[1] and B in route[1] if route[1].index(A) < route[1].index(B)]

with open("cowroute.out", "w") as file2:
    if costs == []:
        print(-1, file=file2)
    else:
        print(min(costs), file=file2)
