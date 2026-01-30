class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print(f"Factors of {self.Value} are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

n1 = Numbers(6)
n2 = Numbers(11)
n3 = Numbers(28)

print("Number:", n1.Value)
print("Is Prime:", n1.ChkPrime())
print("Is Perfect:", n1.ChkPerfect())
n1.Factors()
print("Sum of Factors:", n1.SumFactors())
print()

print("Number:", n2.Value)
print("Is Prime:", n2.ChkPrime())
print("Is Perfect:", n2.ChkPerfect())
n2.Factors()
print("Sum of Factors:", n2.SumFactors())
print()

print("Number:", n3.Value)
print("Is Prime:", n3.ChkPrime())
print("Is Perfect:", n3.ChkPerfect())
n3.Factors()
print("Sum of Factors:", n3.SumFactors())