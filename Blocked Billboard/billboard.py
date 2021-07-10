with open("billboard.in") as input_file:
    b11x, b12y, b12x, b11y = map(int, input_file.readline().split())
    b21x, b22y, b22x, b21y = map(int, input_file.readline().split())
    t1x, t1y, t2x, t2y = map(int, input_file.readline().split())

coords = [[[x, y] for x in range(b11x, b12x+1) for y in range(b12y, b11y+1)], [[x, y] for x in range(b21x, b22x+1) for y in range(b22y, b21y+1)],[[x,y] for x in range(t1x, t2x+1) for y in range(t1y, t2y+1)]]
area1, area2 = (b12x-b11x)*(b11y-b12y), (b22x-b21x)*(b21y-b22y)
maxx1, maxy1, minx1, miny1, maxx2, maxy2, minx2, miny2 = -2000, -2000, 2000, 2000, -2000, -2000, 2000, 2000
common1, common2 = [each for each in coords[2] if each in coords[0]], [each for each in coords[2] if each in coords[1]]

for each in common1:
    if each[0] > maxx1:
        maxx1 = each[0]
    elif each[0] < minx1:
        minx1 = each[0]
    if each[1] > maxy1:
        maxy1 = each[1]
    elif each[1] < miny1:
        miny1 = each[1]

for each in common2:
    if each[0] > maxx2:
        maxx2 = each[0]
    elif each[0] < minx2:
        minx2 = each[0]
    if each[1] > maxy2:
        maxy2 = each[1]
    elif each[1] < miny2:
        miny2 = each[1]

with open("billboard.out", "w") as output_file:
    print((area1-((maxx2-minx2)*(maxy2-miny2)))+(area2-((maxx1-minx1)*(maxy1-miny1))), file=output_file)
