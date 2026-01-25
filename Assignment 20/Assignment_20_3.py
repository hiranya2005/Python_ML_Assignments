import threading

def EvenListSum(arr):

    iSum = 0

    for no in arr:

        if no % 2 == 0:

            iSum = iSum + no

    print("Sum of even list elements is : ", iSum)

def OddListSum(arr):

    iSum = 0

    for no in arr:

        if no % 2 != 0:

            iSum = iSum + no

    print("Sum of OOdd list elements is : ", iSum)


def main():
    
    Value = int(input("Enter a number of elements : "))

    Data = list()

    for i in range (Value):
        
        Data.append(int(input()))


    EvenList = threading.Thread(target= EvenListSum , args=(Data,))
    OddList = threading.Thread(target= OddListSum , args=(Data,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

    print("Exit from main..")

if __name__ == "__main__":
    main()