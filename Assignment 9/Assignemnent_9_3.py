#Q3

def SquareNumber(no):
    
    return no * no

def main():
    
    Value = int(input("Enter a number : "))

    iRet = SquareNumber(Value)

    print("Square of given number is : ", iRet)

if __name__ == "__main__":
    main()