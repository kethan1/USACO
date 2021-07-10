with open("square.in", "r") as input_file:
    x1, y1, x2, y2 = map(int, input_file.readline().split())
    x3, y3, x4, y4 = map(int, input_file.readline().split())

maximum, minimum = [max(x2, x4), max(y2, y4)], [min(x1, x3), min(y1, y3)]

with open("square.out", "w") as output_file:
    print(max((maximum[0] - minimum[0]), (maximum[1] - minimum[1])) * max((maximum[0] - minimum[0]), (maximum[1] - minimum[1])), file=output_file)
