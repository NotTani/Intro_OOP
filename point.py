from math import sqrt, pi

class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(float(self.x), float(self.y))

    def dist_to(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def abs(self):
        return sqrt(self.x**2 + self.y**2)

class Rectangle:
    def __init__(self, p1, p2):
        if type(p1) != Point or type(p2) != Point:
            raise ValueError("Rectangle() needs two Point objects")

        self.c1 = p1
        self.c2 = p2
        self.width = p2.x - p1.x
        self.length = p2.y - p1.y

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return abs((self.width * 2) + (self.length * 2))

    def inside(self, point):
        if self.p1.x <= point.x <= self.p2.x:
            if self.p1.y <= point.y <= self.p2.y:
                return True
        return False

class Circle:
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius

    def area(self):
        return float(pi * self.radius ** 2)

    def perimeter(self):
        return float(self.radius * 2 * pi)

    def inside(self, point):
        if point.dist_to(self.center) <= self.radius:
            return True
        return False

def main():
    p1 = Point(3.0, 4.0)
    print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

    p2 = Point(-1.0, 40)
    print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))

    r = Rectangle(Point(5, 5), Point(0, 0))
    print("A rectangle of the corners {} and {} has a parimeter of {} and an area of {}"
          .format(r.c1, r.c2, r.perimeter(), r.area()))

    c = Circle(Point(0,0), 5)
    print("A circle of originating at {} with a radius of {} has a perimeter of {:.5} and an area of {:.5}"
          .format(c.center, c.radius, c.perimeter(), c.area()))

    print("The point {} is inside the circle: {}".format(p1, c.inside(p1)))
    print("The point {} is inside the circle: {}".format(p2, c.inside(p2)))

if __name__ == "__main__":
    main()
