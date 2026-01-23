#Q10
LargestNum = lambda no1 , no2 , no3: (

    no1 if no1 > no2 and no1 > no3 else
    no2 if no2 > no3 else
    no3
)
def main():

    Value1 = int (input("Enter first number : "))
    Value2 = int (input("Enter second number : "))
    Value3 = int (input("Enter third number : "))

    iRet = LargestNum(Value1 , Value2 , Value3)
    print("Maximum number is : " , iRet)


if __name__ == "__main__":
    main()