#Q3

def PerformMath(no1 , no2 , op):
    
    if ( op == 1):
        return no1 + no2
    elif( op == 2 ):
        return no1 - no2
    elif( op == 3 ):
        
        try:
            Result = float(no1)/float(no2)
            return Result

        except ZeroDivisionError as zobj:
            print("Error : ", zobj)

    else:
        return no1*no2

def main():
    
    try:
        Value1 = int(input("Enter first number : "))
        Value2 = int(input("Enter second number : "))

    except ValueError as vobj:
        print("Error : ", vobj)
        print("Enter a positive integer!")
        return

    print("Operation's to perform")
    print("1 : Addition")
    print("2 : Substraction")
    print("3 : Division")
    print("4 : Multipication")

    while(1):

        try:
            Operation = int(input("Enter Operation Number : "))

        except ValueError as vobj:
            print("Error : ",vobj)
            print("Enter a valid positive integer!")
            break


        if( Operation == 1):
            iRet = PerformMath(Value1 , Value2 , Operation)
            print("Addition is : ",iRet)
            break

        elif( Operation == 2):
            iRet = PerformMath(Value1 , Value2 , Operation)
            print("Substraction is : ",iRet)
            break

        elif( Operation == 3):
            iRet = PerformMath(Value1 , Value2 , Operation)
            print("Division is : ",iRet)
            break

        elif( Operation == 4):
            iRet = PerformMath(Value1 , Value2 , Operation)
            print("Multiplication is : ",iRet)
            break
        else:
            print("Enter a Valid number!")
            break
    

if __name__ == "__main__":

    main()