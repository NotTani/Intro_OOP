from math import sqrt, pi

class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


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
        return True if (self.p1.x <= point.x <= self.p2.x) \
                   and (self.p2.y <= point.y <= self.p2.y)
        return False

class Circle:
    def __init__(self, point, radius):
        self.center = point
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimiter(self):
        return self.radius * 2 * pi

    def inside(self, point):
        if abs(point.x - self.center.x) <= self.radius \
       and abs(point.y - self.center.y) <= self.radius:
            return True
        return False

def main():
    p1 = Point(3.0, 4.0)
    print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

    p2 = Point(-1.0, 6.5)
    print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))

    a = Rectangle(Point(5, 5), Point(0, 0))
    print(a.perimeter())
    

if __name__ == "__main__":
    main()
