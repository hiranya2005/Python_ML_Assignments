class Circle:
    Pi = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius of the circle: "))

    def CalculateArea(self):
        self.Area = Circle.Pi * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.Pi * self.Radius

    def Display(self):
        print("Radius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)


c1 = Circle()
c2 = Circle()

print("Circle 1")
c1.Accept()
c1.CalculateArea()
c1.CalculateCircumference()
c1.Display()

print("Circle 2")
c2.Accept()
c2.CalculateArea()
c2.CalculateCircumference()
c2.Display()