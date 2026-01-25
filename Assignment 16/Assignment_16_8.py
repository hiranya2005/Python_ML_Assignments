#Q8

def PrintStar(no):

    for i in range( no ):
        print("*" , end="\t")
    print()

def main():
    
    Value = int(input("Enter a number : "))

    PrintStar(Value)


if __name__ == "__main__":
    main()