import threading

def DisplaySumEvenFactors(no):

    print("Printing Even")

    iSum = 0
    
    for i in range(1 , no + 1):
        if no % i == 0:
            if i % 2 == 0:
                iSum = iSum + i
                
    print("Sum of even factors is : ", iSum)

def DisplaySumOddFactors(no):

    print("Printing Odd")

    iSum = 0
    
    for i in range(1 , no + 1):
        if no % i == 0:
            if i % 2 != 0:
                iSum = iSum + i
                
    print("Sum of Odd factors is : ", iSum)


def main():
    
    Value = int(input("Enter a number : "))

    EvenFactor = threading.Thread(target= DisplaySumEvenFactors , args=(Value,))
    OddFactor = threading.Thread(target= DisplaySumOddFactors , args=(Value,))

    EvenFactor.start()
    OddFactor.start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main..")

if __name__ == "__main__":
    main()