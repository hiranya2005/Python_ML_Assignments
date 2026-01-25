
def Add(arr):
    
    iSum = 0

    for no in arr:
        iSum = iSum + no
    return iSum

def main():

    Data = list()

    ElementNo = int(input("Enter number of elements : "))

    for i in range(ElementNo):
        Data.append(int(input()))

    iRet = Add(Data)

    print("Addition of elements is : ", iRet)

if __name__ == "__main__":
    main()