#Q4

def PrintBinary(no):
    
    val = no
    Data = []

    while(val > 0):

        if(val % 2 == 0):
            Data.insert(0 , 0)
            val = (val)// 2
        else:
            Data.insert(0 , 1)
            val = (val)//2

    print(Data)

def main():

    Value = int(input("Enter a number : "))

    PrintBinary(Value)

if __name__ == "__main__":
    main()