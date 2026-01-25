#Q1

import Arithematic

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
    print("3 : Multiplication")
    print("4 : Division")

    while(1):

        try:
            Operation = int(input("Enter Operation Number : "))

        except ValueError as vobj:
            print("Error : ",vobj)
            print("Enter a valid positive integer!")
            break


        if( Operation == 1):
            iRet = Arithematic.Add(Value1 , Value2)
            print("Addition is : ",iRet)
            break

        elif( Operation == 2):
            iRet = Arithematic.Sub(Value1 , Value2)
            print("Substraction is : ",iRet)
            break

        elif( Operation == 3):
            iRet = Arithematic.Multiplication(Value1 , Value2 )
            print("Multiplication is : ",iRet)
            break

        elif( Operation == 4):
            iRet = Arithematic.Division(Value1 , Value2 )
            print("Division is : ",iRet)
            break
        else:
            print("Enter a Valid number!")
            break
    

if __name__ == "__main__":

    main()