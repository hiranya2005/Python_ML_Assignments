import os

def CheckWord(FileName , cWord):

    Ret = os.path.exists(FileName)
    if Ret == False:
        print("File does not exists")
        return
    
    Ret = os.path.isdir(FileName)
    if Ret == True:
        print("Please enter file name")
        return

    bFlag = False
    fobj = open(FileName , "r")

    lines = fobj.readlines()

    for i in range(len(lines)):

        words = lines[i].split()

        for word in words:
            if word == cWord:
                bFlag = True
    
    return bFlag


def main():
    Fname = input("Enter the name of file : ")
    word = input('Enter the word you want to search : ')

    Ret = CheckWord(Fname , word)

    if Ret == True:
        print("Given word is present in file...")
    else:
        print("Given word is not present file...")

if __name__ == "__main__":
    main()