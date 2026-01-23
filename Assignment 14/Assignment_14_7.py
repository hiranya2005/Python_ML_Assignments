#Q7
IsDivisible = lambda no : no % 5 == 0

def main():

    bRet = False

    Value = int (input("Enter a number : "))

    bRet = IsDivisible(Value)

    if(bRet == True):
        print(Value,"is is Divisible by 5")
    else:
        print(Value,"is not divisible by 5")

if __name__ == "__main__":
    main()