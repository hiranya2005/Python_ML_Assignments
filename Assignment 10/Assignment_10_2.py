#Q2

def SumOfFirstN(no):
    sum = 0

    for i in range(1 , no+1):
        sum = sum + i

    return sum

def main():
    
    Value = int(input("Enter a number : "))

    iRet = SumOfFirstN(Value)

    print("Sum of first N numbers is : ", iRet)

if __name__ == "__main__":
    main()