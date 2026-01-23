#Q9
Multiplication = lambda no1 , no2 : no1 * no2

def main():

    iRet = 0

    Value1 = int (input("Enter first number : "))
    Value2 = int (input("Enter second number : "))

    iRet = Multiplication(Value1 , Value2)

    print("Multiplication is : ",iRet)

if __name__ == "__main__":
    main()