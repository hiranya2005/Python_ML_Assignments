#Q3

def SumDigits(no):
    sum = 0
    iDigit = 0

    if( no < 0):
        print("Enter a valid Number!")
        return

    while(no != 0):
        
        iDigit = no % 10
        sum = sum + iDigit
        no = no // 10

    return sum
def main():
    
    Value = int(input("Enter a number : "))

    iRet = SumDigits(Value)

    print("Number of digits in given number are : ",iRet)


if __name__ == "__main__":
    main()