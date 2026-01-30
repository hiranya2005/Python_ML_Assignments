class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter first value: "))
        self.Value2 = float(input("Enter second value: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not allowed"
        else:
            return self.Value1 / self.Value2



a1 = Arithmetic()
a2 = Arithmetic()

print("Arithmetic Object 1")
a1.Accept()
print("Addition :", a1.Addition())
print("Subtraction :", a1.Subtraction())
print("Multiplication :", a1.Multiplication())
print("Division :", a1.Division())

print("Arithmetic Object 2")
a2.Accept()
print("Addition :", a2.Addition())
print("Subtraction :", a2.Subtraction())
print("Multiplication :", a2.Multiplication())
print("Division :", a2.Division())