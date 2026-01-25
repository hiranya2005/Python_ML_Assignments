
def FindFrequency(arr , iSearch):
    
    iFreq = 0
    for no in arr:
        if no == iSearch:

            iFreq = iFreq + 1

    return iFreq

def main():

    Data = list()

    ElementNo = int(input("Enter number of elements : "))

    for i in range(ElementNo):
        Data.append(int(input()))
    
    Value = int(input("Enter element to find frequency : "))

    iRet = FindFrequency(Data , Value)

    print("Fequency is : ", iRet)

if __name__ == "__main__":
    main()