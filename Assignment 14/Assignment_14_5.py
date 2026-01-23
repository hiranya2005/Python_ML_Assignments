#Q5
CheckEven = lambda no : no % 2 == 0

def main():

    bRet = False

    Value = int (input("Enter a number : "))

    bRet = CheckEven(Value)

    if(bRet == True):
        print(Value,"is Even")
    else:
        print(Value,"is Odd")

if __name__ == "__main__":
    main()