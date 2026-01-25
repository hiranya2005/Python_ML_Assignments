from functools import reduce

def FilterX(no):
    
    for i in range(2 , no // 2 + 1):
        if(no % i == 0):
            return False
    return True

def MapX(no):
    
    return no * 2

def ReduceX(no1 , no2):
    
    if( no1 > no2):
        return no1
    else:
        return no2

def main():

    ElementNo = int(input("Enter Number of elements : "))

    Data = list()

    for i in range(1 , ElementNo + 1):

        Data.append(int(input()))

    fData = list(filter(FilterX , Data))
    print("Filter : ",fData)

    mData = list(map(MapX , fData))
    print("Map : ",mData)

    rData = reduce(ReduceX , mData)
    print("Reduce : ",rData)

if __name__ == "__main__":
    main()