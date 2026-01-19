#Q2

def PrintFactors(no):
    
    for i in range(1 , (no+2)//2):              
        if( no % i == 0):
            print(i)
    print(no)
    
def main():
    
    Value = int(input("Enter a number : "))

    PrintFactors(Value)

if __name__ == "__main__":
    main()