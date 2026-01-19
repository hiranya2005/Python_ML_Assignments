#Q5

def CheckPalindrome(no):
    iDigit = 0
    check = list()
    val = no
    i = 0

    if( no <= 0 ):
        print("Enter a valid number")
        return
    
    while(val != 0):
        
        iDigit = val % 10
        check.append(iDigit)
        val = val // 10

    val = no

    for iCnt in range(len(check)):
        
        if ( val % 10 == check[iCnt]):
            val = val // 10
            
            if(val == 0):
                print("Given number is palindrome")
        else:
            print("Given number is not palindrome")
            break

def main():
    
    Value = int(input("Enter a number : "))

    CheckPalindrome(Value)


if __name__ == "__main__":
    main()