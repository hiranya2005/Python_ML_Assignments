import os
import sys
import time
import shutil

def CopyDirectory(DirectoryName , NewDirectory):

    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("Directory Does not exists...")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("ERROR : Enter a valid Directory name")

    Ret = os.path.exists(NewDirectory)
    if Ret == True:
        print(f"{NewDirectory} Directory already exists...")
        return

    os.mkdir(NewDirectory)

    Files = os.listdir(DirectoryName)

    for fname in Files:

        shutil.copy2(os.path.join(DirectoryName , fname) , NewDirectory)

    CreateLogFile(Files , NewDirectory , DirectoryName)
    

def CreateLogFile(Data , nDirectory , oDirectory):

    Border = "-"*40
    FileName = "LogFile%s"%(time.ctime())

    fobj = open(FileName , "w")
    fobj.write(Border + "\n")
    fobj.write("--------------- Log File ---------------\n")
    fobj.write(Border + "\n")
    fobj.write(f"Below File Copied Successfully from {oDirectory} to {nDirectory} "+"\n")
    for name in Data:
        fobj.write(name + "\n")

    fobj.write(Border + "\n")
    fobj.write("--------------- Log File ---------------\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():
    
    if len(sys.argv) != 3:
        print("Invalid Number of Arguments...")
        return

    CopyDirectory(sys.argv[1] , sys.argv[2]) 


if __name__ == "__main__":
    main()