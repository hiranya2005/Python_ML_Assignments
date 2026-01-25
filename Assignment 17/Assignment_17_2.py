#Q2

def DisplayPattern(no):

    row = no
    column = no

    for i in range(row):
        print()
        for j in range(column):
            print("*" , end="\t")
    print()

def main():

    Value = int(input("Enter a number : "))
    DisplayPattern(Value)

if __name__ == "__main__":
    main()