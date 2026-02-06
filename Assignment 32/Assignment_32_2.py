import os
import sys
import hashlib

def DuplicateFiles(FileName):

    fobj = open(FileName , "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(100)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(100)

    fobj.close()
    return hobj.hexdigest()

def OpenDir(DirectoryName):

    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("Directory Does not Exists...")
        return
    
    Ret = os.path.isfile(DirectoryName)
    if Ret == True:
        print("Enter Directory Name...")
        return
    
    Data = list()
    Duplicate = {}
    for FolderName , SubFolderName , FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName , fname)   
            CheckSum = DuplicateFiles(fname)
            fname = os.path.relpath(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)

            else:
                Duplicate[CheckSum] = [fname]

    Result = list(filter(lambda x : len(x) > 1 , Duplicate.values()))

    for names in Result:
        if len(names) > 1:
            for name in names:
                Data.append(name)

    CreateLogFile(Data , DirectoryName)

def CreateLogFile(Data , DirName):

    DirName = os.path.relpath(DirName)

    FileName = "Log.txt"
    Border  = "-"*40

    dfobj = open(FileName , "w")

    dfobj.write(Border + "\n")
    dfobj.write("--------------- Log File ---------------\n")
    dfobj.write(Border + "\n")

    dfobj.write(f"Copy Files in \'{DirName}\' are : \n")
    for cSum in Data:
        dfobj.write(cSum + "\n")

    dfobj.write(Border + "\n")
    dfobj.write("--------------- Log File ---------------\n")
    dfobj.write(Border + "\n")

    dfobj.close()



def main():
    
    if len(sys.argv) == 2:
        sys.argv[1] = os.path.abspath(sys.argv[1])
        OpenDir(sys.argv[1])
    else:
        print("Invalid Number of Arguments...")

if __name__ == "__main__":
    main()