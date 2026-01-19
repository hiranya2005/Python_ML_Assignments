#Q1
def CheckCharacter(ch):

    if( ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' ):
        return True
    
    elif (ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
        return True
    
    else:
        return False

def main():
    
    bRet = False
    char = input("Enter a character : ")

    bRet = CheckCharacter(char)

    if(bRet == True):
        print(char,"is a vowel")
    else:
        print(char,"is a consonant")


if __name__ == "__main__":
    main()