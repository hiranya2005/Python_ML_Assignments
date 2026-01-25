#Q10

def Display(no):
    
    iSum = 0
    iDigit = 0

    while( no != 0):

        iDigit = no % 10
        iSum = iSum + iDigit
        no = no // 10
    return iSum

def main():

    Value = int(input("Enter a number : "))
    iRet = Display(Value)

    print("Sum of Digits is : ", iRet)


if __name__ == "__main__":
    main()