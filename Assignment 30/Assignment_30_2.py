import os

def CountWords(FileName):
    
    Ret = os.path.exists(FileName)
    if Ret == False:
        print("File does not exists")
        return
    
    Ret = os.path.isdir(FileName)
    if Ret == True:
        print("Please enter file name")
        return
    
    iCount = 0
    fobj = open(FileName , "r")

    Buffer = fobj.readlines()

    for i in range(len(Buffer)):

        words = Buffer[i].split()

        for _ in words:
            iCount = iCount + 1
    
    print(iCount)

    fobj.close()

def main():
    
    Fname = input("Enter the name of file : ")
    CountWords(Fname)

if __name__ == "__main__":
    main()