#Q1

def PrintTable(no):
    
    for i in range (1 , 11):
        print(no,"x",i,"=",no*i)

def main():
    
    Value = int(input("Enter a number : "))

    PrintTable(Value)

if __name__ == "__main__":
    main()