
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


def distance(p1, p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5


start_point = Point(0, 0)
start_dist = 0
for char in points:
    res = distance(start_point, char)
    if res > start_dist:
        max_dist = start_dist
        max_point = char

    print("Координаты наиболее удаленной точки = ", max_point.x, max_point.y)