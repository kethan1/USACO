with open("factory.in") as input_file:
    N = int(input_file.readline())
    walkways = [list(map(int, line.split())) for line in input_file]

graph = {
    station_num: []
    for station_num in range(1, N + 1)
}
for walkway in walkways:
    graph[walkway[0]].append(walkway[1])


def pathPossible(starting, ending):
    if starting == ending:
        return True
    return bool(sum(pathPossible(newStarting, ending) for newStarting in graph[starting]))


for ending in range(1, N + 1):
    possible = True
    for starting in range(1, N + 1):
        if not pathPossible(starting, ending):
            possible = False
    if possible:
        break

with open("factory.out", "w") as output_file:
    if possible:
        print(ending, file=output_file)
    else:
        print(-1, file=output_file)
