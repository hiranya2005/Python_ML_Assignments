#Q5

def PrintNumber(no):
    
    for i in range(no , 0 , -1): 
        print(i)             
    
def main():
    
    Value = int(input("Enter a number : "))

    PrintNumber(Value)

if __name__ == "__main__":
    main()