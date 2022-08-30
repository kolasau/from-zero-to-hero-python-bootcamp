from math import pi


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return (y2 - y1) / (x2 - x1)


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        height = self.height
        radius = self.radius
        return pi * (radius**2) * height

    def surface_area(self):
        height = self.height
        radius = self.radius
        return (2 * pi * radius * height) + (2 * pi * (radius**2))


#             (x, y)
coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())

c = Cylinder(2, 3)
print(c.volume())
print(c.surface_area())
