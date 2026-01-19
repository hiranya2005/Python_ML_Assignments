#Q3

def CheckPerfect(no):
    
    isum = 0

    for i in range(1 , (no+2)//2):
        if(no % i == 0):
            isum = isum + i
    
    if( isum == no ):
        return True
    else:
        return False

def main():
    
    bRet = False

    Value = int(input("Enter a number : "))

    bRet = CheckPerfect(Value)

    if(bRet == True):
        print(Value,"is a perfect number.")
    else:
        print(Value,"is not a perfect number.")

if __name__ == "__main__":
    main()