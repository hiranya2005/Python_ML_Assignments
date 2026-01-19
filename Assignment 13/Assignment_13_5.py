#Q5

def DisplayGrade(no):
    
    if( no >= 75 ):
        print("Distinction")
    elif( no >= 60 and no < 75):
        print("First class")
    elif( no >= 50 and no < 60):
        print("Second class")
    else:
        print("Fail")

def main():

    Value = int(input("Enter Marks : "))

    DisplayGrade(Value)

if __name__ == "__main__":
    main()