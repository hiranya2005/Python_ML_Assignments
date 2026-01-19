#Q4

def CubeNumber(no):
    
    return no * no * no

def main():
    
    Value = int(input("Enter a number : "))

    iRet = CubeNumber(Value)

    print("Cube of given number is : ", iRet)

if __name__ == "__main__":
    main()