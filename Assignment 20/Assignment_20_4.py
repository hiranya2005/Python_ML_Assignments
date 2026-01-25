import threading

def CountSmall(arr):

    print("Thread id of Small : ", threading.get_ident())
    iCount = 0

    for no in arr:

        if no >= 'a' and no <= 'z':
            iCount = iCount + 1

    print("Count of lower case characters are : ", iCount)

def CountCapital(arr):

    print("Thread id of Capital : ", threading.get_ident())
    iCount = 0

    for no in arr:

        if no >= 'A' and no <= 'Z':
            iCount = iCount + 1

    print("Count of Upper case characters are : ", iCount)


def CountDigit(arr):

    print("Thread id of Digit : ", threading.get_ident())

    iCount = 0

    for no in arr:

        if no >= '0' and no <= '9':
            iCount = iCount + 1

    print("Count of Digits are : ", iCount)


def main():
    
    print("Thread id of main : ", threading.get_ident())

    Data = input("Enter a string : ")

    Small = threading.Thread(target= CountSmall , args=(Data,))
    Capital = threading.Thread(target= CountCapital , args=(Data,))
    Digits = threading.Thread(target= CountDigit , args=(Data,))


    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from main..")


if __name__ == "__main__":
    main()