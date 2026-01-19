#Q4

def PrintNumber(no):
    
    for i in range(1 , (no+1)): 
        print(i)             
    
def main():
    
    Value = int(input("Enter a number : "))

    PrintNumber(Value)

if __name__ == "__main__":
    main()