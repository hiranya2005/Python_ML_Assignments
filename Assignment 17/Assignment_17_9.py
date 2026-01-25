#Q9

def Display(no):
    
    iCount = 0

    while( no != 0):

        iCount = iCount + 1
        no = no // 10
    return iCount

def main():

    Value = int(input("Enter a number : "))
    iRet = Display(Value)

    print("Number of digits in the given number is : ", iRet)


if __name__ == "__main__":
    main()