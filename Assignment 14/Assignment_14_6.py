#Q6
CheckOdd = lambda no : no % 2 != 0

def main():

    bRet = False

    Value = int (input("Enter a number : "))

    bRet = CheckOdd(Value)

    if(bRet == True):
        print(Value,"is Odd")
    else:
        print(Value,"is Even")

if __name__ == "__main__":
    main()