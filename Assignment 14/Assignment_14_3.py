#Q3
IsGreater = lambda no1 , no2 : no1 > no2

def main():

    bRet = False

    Value1 = int (input("Enter a number : "))
    Value2 = int (input("Enter another number : "))

    bRet = IsGreater(Value1 , Value2)

    if(bRet == True):
        print(Value1,"is maximum")
    else:
        print(Value2,"is maximum")

if __name__ == "__main__":
    main()