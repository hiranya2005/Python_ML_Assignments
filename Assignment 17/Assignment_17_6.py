#Q6

def Display(no):
    
    for i in range(no):
        print()
        for j in range(i , no):
            print("*" , end="\t") 
    print()


def main():

    Value = int(input("Enter a number : "))
    Display(Value)


if __name__ == "__main__":
    main()