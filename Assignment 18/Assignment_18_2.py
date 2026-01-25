
def Maximum(arr):
    
    iMax = arr[0]

    for no in arr:
        if no > iMax:
            iMax = no
    return iMax

def main():

    Data = list()

    ElementNo = int(input("Enter number of elements : "))

    for i in range(ElementNo):
        Data.append(int(input()))

    iRet = Maximum(Data)

    print("Maximum is : ", iRet)

if __name__ == "__main__":
    main()