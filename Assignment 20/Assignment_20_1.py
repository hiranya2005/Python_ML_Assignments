import threading

def PrintEven():

    print("Printing Even")

    for i in range(1 , 21):

        if i % 2 == 0:
            print(i)

def PrintOdd():

    print("Printing Odd")

    for i in range(1 , 20):

        if i % 2 != 0:
            print(i)

def main():
    
    Even = threading.Thread(target= PrintEven)
    Odd = threading.Thread(target= PrintOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()