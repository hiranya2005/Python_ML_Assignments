#Q1

def AreaOfRectangle(length , width):
    
    return length*width


def main():
    
    Value1 = int(input("Enter length : "))
    Value2 = int(input("Enter Width : "))

    iRet = AreaOfRectangle(Value1 , Value2)

    print("Area of Rectangle : ",iRet)

if __name__ == "__main__":
    main()