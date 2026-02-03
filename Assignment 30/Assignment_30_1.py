import os

def CountLines(FileName):

    iCount = 0
    ret = os.path.exists(FileName)

    if ret == False:
        print('File does not exist...')
        return
    
    ret = os.path.isdir(FileName)
    if ret == True:
        print("please enter file name...")
        return
    
    fobj = open(FileName , "r")

    lCount = fobj.readlines()

    for line in lCount:
        if line != "\n":
            iCount = iCount + 1

    print(iCount)

    fobj.close()

def main():

    Fname = input("Enter the name of file : ")
    CountLines(Fname)

if __name__ == "__main__":
    main()
