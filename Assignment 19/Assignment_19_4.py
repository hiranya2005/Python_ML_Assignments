from functools import reduce

FilterX = lambda no :  no % 2 == 0
MapX = lambda no : no**2
ReduceX = lambda no1 , no2 : no1 + no2

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