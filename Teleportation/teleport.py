with open("teleport.in") as input_file:
    a, b, x, y = map(int, input_file.readline().split())

dis = 0

closest_to_a = min([b, x, y], key=lambda x: abs(x - a))

if closest_to_a == b:
    dis += abs(b - a)
else:
    if closest_to_a == x:
        if abs(a - x) + abs(b - y) > abs(b - a):
            dis += abs(b - a)
        else:
            dis += abs(a - x) + abs(b - y)
    else:
        if abs(a - y) + abs(b - x) > abs(b - a):
            dis += abs(b - a)
        else:
            dis += abs(a - y) + abs(b - x)

with open("teleport.out", "w") as output_file:
    print(dis, file=output_file)
