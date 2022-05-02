import itertools

with open("triangles.in") as input_file:
    N = int(input_file.readline())
    points = []
    for point in input_file:
        x, y = map(int, point.split())
        points.append((x, y))

max_area = 0

for fence_posts in itertools.combinations(points, 3):
    fence_post_1, fence_post_2, fence_post_3 = fence_posts
    if len({fence_post_1, fence_post_2, fence_post_3}) != 3:
        continue
    fence_post_1_x, fence_post_1_y = fence_post_1
    fence_post_2_x, fence_post_2_y = fence_post_2
    fence_post_3_x, fence_post_3_y = fence_post_3
    width = height = 0
    if fence_post_1_x == fence_post_2_x:
        width = abs(fence_post_1_y - fence_post_2_y)
        if fence_post_1_y == fence_post_3_y:
            height = abs(fence_post_1_x - fence_post_3_x)
        elif fence_post_2_y == fence_post_3_y:
            height = abs(fence_post_2_x - fence_post_3_x)
    elif fence_post_2_x == fence_post_3_x:
        width = abs(fence_post_2_y - fence_post_3_y)
        if fence_post_1_y == fence_post_2_y:
            height = abs(fence_post_1_x - fence_post_2_x)
        elif fence_post_1_y == fence_post_3_y:
            height = abs(fence_post_1_x - fence_post_3_x)
    elif fence_post_1_x == fence_post_3_x:
        width = abs(fence_post_1_y - fence_post_3_y)
        if fence_post_2_y == fence_post_3_y:
            height = abs(fence_post_2_x - fence_post_3_x)
        elif fence_post_1_y == fence_post_2_y:
            height = abs(fence_post_1_x - fence_post_2_x)
    max_area = max(max_area, width * height)

with open("triangles.out", "w") as output_file:
    print(max_area, file=output_file)
