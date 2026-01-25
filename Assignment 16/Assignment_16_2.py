#Q2
def CheckNum(no):

    if(no %2 == 0):
        return True
    else:
        return False

def main():
    
    bRet = False
    Value = int(input("Enter a number : "))

    bRet = CheckNum(Value)

    if(bRet == True):
        print("Given number is Even")
    else:
        print("Given number is Odd")

if __name__ == "__main__":
    main()