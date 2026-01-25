#Q7

def CheckDivisible(no):

    if( no % 5 == 0):
        return True
    else:
        return False


def main():
    
    Value = int(input("Enter a number : "))

    bRet = CheckDivisible(Value)

    if(bRet == True):
        print("Given number is divisible by 5")
    else:
        print("Given number is not divisible by 5")

if __name__ == "__main__":
    main()