#Q8
Addition = lambda no1 , no2 : no1 + no2

def main():

    iRet = 0

    Value1 = int (input("Enter first number : "))
    Value2 = int (input("Enter second number : "))

    iRet = Addition(Value1 , Value2)

    print("Addition is : ",iRet)

if __name__ == "__main__":
    main()