import os
import sys
import hashlib

def FindCheckSum(FileName):

    fobj = open(FileName , "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(100)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(100)

    fobj.close()
    return hobj.hexdigest()


def OpenFile(DirectoryName):
    
    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("There no such Directory...")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("There no such Directory...")
        return
    
    Duplicate = {}

    for FolderName , SubFolderName , FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName , fname)
            CheckSum = FindCheckSum(fname)
            fname = os.path.relpath(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]

    DeleteDuplicate(Duplicate)
    
def DeleteDuplicate(Data):

    iCount = 0
    cnt = 0
    Result = list(filter(lambda x : len(x) > 1 , Data.values()))
    DuplicateName = list()

    for values in Result:
            for value in values:
                iCount = iCount + 1
                if iCount > 1:
                    name = value
                    DuplicateName.append(name)
                    os.remove(value)
                    cnt = cnt + 1

    CreatLogFile(DuplicateName , cnt)

def CreatLogFile(Fname , count):

    FileName = "Log.txt"
    Border = "-"*40

    lobj = open(FileName , "w")

    lobj.write(Border+"\n")
    lobj.write("---------------- Log File ----------------\n")
    lobj.write(Border+"\n")

    lobj.write("Total number of files deleted : " + str(count)+"\n")

    for name in Fname:

        lobj.write(name+"\n")

    lobj.write(Border+"\n")
    lobj.write("---------------- Log File ----------------\n")
    lobj.write(Border+"\n")


def main():

    if len(sys.argv) == 2:
        sys.argv[1] = os.path.abspath(sys.argv[1])
        OpenFile(sys.argv[1])
    else:
        print("Invalid number of Arguments....")
        return


if __name__ == "__main__":
    main()