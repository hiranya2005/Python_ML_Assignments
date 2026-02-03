import os
def CompareString(FileName , Str):

    iRet = os.path.exists(FileName)

    if iRet == False:
        print("File Does not exists...")
        return

    iCount = 0
    fobj = open(FileName , "r")

    File_size = os.path.getsize(FileName)

    Buffer = fobj.read(File_size)

    split = Buffer.split()

    for words in split:
        if Str == words:
            iCount = iCount + 1

    return iCount

def main():
   
   Fname = input("Enter File name : ")
   Data = input("Enter String :")

   Ret = CompareString(Fname , Data)

   print(Ret)

if __name__ == "__main__":
    main()