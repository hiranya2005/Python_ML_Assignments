#Q3
def Add(no1 , no2):

    Result = 0

    Result = no1 + no2

    return Result

def main():
    
    iRet = 0
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter Second number : "))

    iRet = Add(Value1 , Value2)

    print("Addition is : ",iRet)

if __name__ == "__main__":
    main()