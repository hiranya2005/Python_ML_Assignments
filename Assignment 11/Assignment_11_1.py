#Q1

def CheckPrime(no):
    
    for i in range (2 , no):
        if( no % i == 0 ):
            return False
        
    return True

def main():
    
    Value = int(input("Enter a number : "))

    bRet = CheckPrime(Value)

    if(bRet == True):
        print(Value,"is a Prime number")
    else:
        print(Value,"is not a Prime number")


if __name__ == "__main__":
    main()