#Q4

def AddFactors(no):

    iSum = 0

    for i in range(1 , (no//2)+1):
       if(no % i == 0):
           iSum = iSum + i

    return iSum

def main():

    Value = int(input("Enter a number : "))
    iRet = AddFactors(Value)

    print("Addition of factors is : ",iRet)

if __name__ == "__main__":
    main()