with open("lostcow.in") as input_file:
    x, y = map(int, input_file.readline().split())

current_position_from_x = 1
distance = 1

while True:
    if x <= y and x + current_position_from_x >= y:
        distance += y - (x + current_position_from_x)
        break
    elif x >= y and x + current_position_from_x <= y:
        distance += (x + current_position_from_x) - y
        break

    distance += abs(current_position_from_x - (-2 * current_position_from_x))
    current_position_from_x *= -2

with open("lostcow.out", "w") as output_file:
    output_file.write(str(distance))
