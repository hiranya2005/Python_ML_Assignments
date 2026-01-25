
def Minimum(arr):
    
    iMin = arr[0]

    for no in arr:
        if no < iMin:
            iMin = no
    return iMin

def main():

    Data = list()

    ElementNo = int(input("Enter number of elements : "))

    for i in range(ElementNo):
        Data.append(int(input()))

    iRet = Minimum(Data)

    print("Minimum is : ", iRet)

if __name__ == "__main__":
    main()