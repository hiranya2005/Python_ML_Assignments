#Q3

def Factorial(no):
    Fact = 1

    for i in range(1,no+1):
        Fact = Fact * i

    return Fact

def main():
    
    Value = int(input("Enter a number : "))

    iRet = Factorial(Value)

    print("Factorial is : ", iRet)

if __name__ == "__main__":
    main()