#Q2
from math import pi

def AreaOfCircle(radius):
    
    return pi*radius**2


def main():
    
    Value = int(input("Enter radius : "))

    iRet = AreaOfCircle(Value)

    print("Area of Circle : ",iRet)

if __name__ == "__main__":
    main()