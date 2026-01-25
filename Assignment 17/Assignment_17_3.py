#Q3

def Factorial(no):

    iFact = 1

    for i in range(1 , no + 1):
        iFact = iFact * i

    return iFact

def main():

    Value = int(input("Enter a number : "))
    iRet = Factorial(Value)

    print("Factorial is : ",iRet)

if __name__ == "__main__":
    main()