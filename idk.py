class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159265359
        pass
    def permiter(self):
        return 2 * self.pi * self.radius
    def area(self):
        return self.pi * self.radius ** 2
radius = float(input("Please enter the radius: "))
circle = Circle(radius)
print(circle.permiter())
print(circle.area())