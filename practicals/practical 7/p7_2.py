# class circle with radius and diameter and methods to calulate area and perimeter
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    radius = int(input("Enter radius of circle: "))
    c = Circle(radius)
    print(c.area())
    print(c.perimeter())
