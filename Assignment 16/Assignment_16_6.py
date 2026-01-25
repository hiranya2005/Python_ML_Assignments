#Q6

def ChkPosNegZero(no):

    if( no > 0 ):
        return "positive"
    elif( no < 0):
        return "negetive"
    else:
        return "zero"

def main():
    
    Value = int(input("Enter a number : "))

    bRet = ChkPosNegZero(Value)

    if(bRet == "positive"):
        print("Given number is positive")
    elif(bRet == "negetive"):
        print("Given number is negetive")
    else:
        print("Given number is zero")

if __name__ == "__main__":
    main()