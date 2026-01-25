#Q8

def Display(no):
    
    for i in range(1 , no+1):
        print()
        for j in range(1 , i+1):
            print(j , end="\t") 
    print()


def main():

    Value = int(input("Enter a number : "))
    Display(Value)


if __name__ == "__main__":
    main()