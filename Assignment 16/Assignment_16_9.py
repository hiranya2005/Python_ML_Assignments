#Q9

def PrintEven():
   
    for i in range(2 ,21):
        if( i % 2 == 0):
            print(i , end="\t")
    print()

def main():

    PrintEven()


if __name__ == "__main__":
    main()