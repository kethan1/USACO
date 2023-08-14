with open("billboard.in") as input_file:
    b1x1, b1y1, b1x2, b1y2 = map(int, input_file.readline().split())
    b2x1, b2y1, b2x2, b2y2 = map(int, input_file.readline().split())
    tx1, ty1, tx2, ty2 = map(int, input_file.readline().split())


class Point:
    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord


class Rectangle:
    def __init__(self, bottom_left, top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right

    def intersects(self, other):
        return not (
            self.top_right.x < other.bottom_left.x
            or self.bottom_left.x > other.top_right.x
            or self.top_right.y < other.bottom_left.y
            or self.bottom_left.y > other.top_right.y
        )

    def area(self):
        return (self.top_right.x - self.bottom_left.x) * (
            self.top_right.y - self.bottom_left.y
        )

    def overlap(self, other):
        if not self.intersects(other):
            return 0

        x_overlap = max(
            0,
            min(self.top_right.x, other.top_right.x)
            - max(self.bottom_left.x, other.bottom_left.x),
        )
        y_overlap = max(
            0,
            min(self.top_right.y, other.top_right.y)
            - max(self.bottom_left.y, other.bottom_left.y),
        )

        return x_overlap * y_overlap


b1 = Rectangle(Point(b1x1, b1y1), Point(b1x2, b1y2))
b2 = Rectangle(Point(b2x1, b2y1), Point(b2x2, b2y2))
t = Rectangle(Point(tx1, ty1), Point(tx2, ty2))

area_visible = b1.area() - b1.overlap(t) + b2.area() - b2.overlap(t)

with open("billboard.out", "w") as output_file:
    print(area_visible, file=output_file)
