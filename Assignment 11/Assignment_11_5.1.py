#Q5

def CheckPalindrome(no):
    iDigit = 0
    Reverse = 0
    val = no

    if( no < 0 ):
        print("Enter a valid number")
        return
    
    while( val != 0 ):

        iDigit = val % 10
        Reverse = Reverse * 10 + iDigit
        val = val // 10

    if Reverse == no :
        print("Given number is palindrome")
    else:
        print("Given number is not palindrome")

def main():
    
    Value = int(input("Enter a number : "))

    CheckPalindrome(Value)


if __name__ == "__main__":
    main()