with open("milkorder.in") as input_file:
    N, M, K = map(int, input_file.readline().split())
    hierarchy = list(map(int, input_file.readline().split()))
    positions = {int(line.split()[0]): int(line.split()[1]) for line in input_file}

order = [0] * N
for cow, position in positions.items():
    order[position - 1] = cow

for index, placed_cow in reversed(list(enumerate(order))):
    if placed_cow != 0 and placed_cow in hierarchy:
        for cow in reversed(hierarchy[:hierarchy.index(placed_cow)]):
            if cow not in order:
                for pos_index, position in reversed(list(enumerate(order[:index]))):
                    if position == 0:
                        order[pos_index] = cow
                        break

answer = 0
if 1 in order:
    answer = order.index(1)
elif 1 in hierarchy:
    if hierarchy[0] not in order:
        for pos, cow in enumerate(order):
            if cow == 0:
                order[pos] = hierarchy[0]
                break
    if 1 not in order:
        for prev_cow_in_order in reversed(hierarchy[:hierarchy.index(1)]):
            if prev_cow_in_order in order:
                break
        for index, cow in list(enumerate(hierarchy))[hierarchy.index(prev_cow_in_order) + 1:]:
            for position, occupier in list(enumerate(order))[order.index(prev_cow_in_order) + 1:]:
                if occupier == 0:
                    order[position] = cow
                    break
    answer = order.index(1)
else:
    answer = order.index(0)

with open("milkorder.out", "w") as output_file:
    print(answer + 1, file=output_file)
