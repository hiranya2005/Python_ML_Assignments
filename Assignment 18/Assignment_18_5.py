import MarvellousNum

def SumElements(arr):
    
    iSum = 0
    for no in arr:

        Ret = MarvellousNum.ChkPrime(no)
        
        if Ret == True:
            iSum = iSum + no

    return iSum

def main():

    Data = list()

    ElementNo = int(input("Enter number of elements : "))

    for i in range(ElementNo):
        Data.append(int(input()))

    iRet = SumElements(Data)

    print("Sum is : ", iRet)

if __name__ == "__main__":
    main()