with open("mowing.in") as mowing_in:
    N = int(mowing_in.readline())
    pattern = [[split_line[0], int(split_line[1])] for line in mowing_in for split_line in [line.split()]]

cells_visited = [[0,0,0]]
revisited_cells = []
for move in pattern:
    cells_visited.append(cells_visited[-1].copy())
    for i in range(1, move[1]+1):
        if move[0] == "N":
            cells_visited[-1][1] += 1
        elif move[0] == "E":
            cells_visited[-1][0] += 1
        elif move[0] == "S":
            cells_visited[-1][1] -= 1
        elif move[0] == "W":
            cells_visited[-1][0] -= 1
        cells_visited[-1][2]+=1
        cells_visited.append(cells_visited[-1].copy())

for index, cell in enumerate(cells_visited):
    for cell2 in cells_visited[index:]:
        if cell[:2] == cell2[:2]:
            if cell2[2] - cell[2] != 0:
                revisited_cells.append(cell2[2] - cell[2])

with open("mowing.out", "w") as mowing_out:
    if revisited_cells:
        print(min(revisited_cells), file=mowing_out)
    else:
        print(-1, file=mowing_out)
