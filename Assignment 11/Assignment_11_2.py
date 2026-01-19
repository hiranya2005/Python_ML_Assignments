#Q2

def CountDigits(no):
    iCount = 0

    while(no != 0):
        iCount = iCount + 1
        no = no // 10

    return iCount
def main():
    
    Value = int(input("Enter a number : "))

    iRet = CountDigits(Value)

    print("Number of digits in given number are : ",iRet)


if __name__ == "__main__":
    main()