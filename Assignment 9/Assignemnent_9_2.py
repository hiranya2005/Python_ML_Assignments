#Q2

def ChkGreater(no1 , no2):

    if( no1 > no2 ):
        return no1
    else :
        return no2

def main():
    
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    iRet = ChkGreater(Value1 , Value2)

    print("Greater number is : ", iRet)

if __name__ == "__main__":
    main()