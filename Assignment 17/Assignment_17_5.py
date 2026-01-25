#Q5

def CheckPrime(no):

    bFlag = True

    for i in range(2 , (no//2)+1):
       if(no % i == 0):
           bFlag = False
           break

    return bFlag

def main():


    Value = int(input("Enter a number : "))
    bRet = CheckPrime(Value)

    if( bRet == True):
        print("Given number is prime number")
    else:
        print("Given number is not a prime number")


if __name__ == "__main__":
    main()