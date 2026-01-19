#Q5
def CheckDiivisible(no):
    
    if( no % 3 == 0 ):
        if(no % 5 == 0):
            return True

    return False

def main():
    
    Value = int(input("Enter a number : "))

    bRet = CheckDiivisible(Value)

    if( bRet == True ):
        print(Value,"is Divisble by 3 & 5.")
    else:
        print(Value,"is Not Divisble by 3 & 5.")

if __name__ == "__main__":
    main()