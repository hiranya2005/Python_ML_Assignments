import os
import sys
import hashlib
import time

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
    
    Start_Time = time.time()

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

    

    DeleteDuplicate(Duplicate , Start_Time)
    
def DeleteDuplicate(Data , sTime):

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
    
    End_Time = time.time()

    Final_Time = End_Time - sTime

    CreatLogFile(DuplicateName , cnt , Final_Time)

def CreatLogFile(Fname , count , ExecutionTime):

    FileName = "Log.txt"
    Border = "-"*40

    lobj = open(FileName , "w")

    lobj.write(Border+"\n")
    lobj.write("--------------- Log File ---------------\n")
    lobj.write(Border+"\n")

    lobj.write("Execution time : " +str(ExecutionTime)+ "\n")
    lobj.write("Total number of files deleted : " + str(count)+"\n")

    for name in Fname:

        lobj.write(name+"\n")

    lobj.write(Border+"\n")
    lobj.write("--------------- Log File ---------------\n")
    lobj.write(Border+"\n")

    lobj.close()

def main():

    if len(sys.argv) == 2:
        sys.argv[1] = os.path.abspath(sys.argv[1])
        OpenFile(sys.argv[1])
    else:
        print("Invalid number of Arguments....")
        return


if __name__ == "__main__":
    main()