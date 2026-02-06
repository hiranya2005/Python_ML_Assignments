import os
import sys
import time

def DsiplayFileExtension(DirectoryName , ExtensionName):

    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("Directory Does not exists...")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("ERROR : Enter a valid Directory name")
    
    Data = list()

    for FolderName , SubFolderName , FileName in os.walk(DirectoryName):
        for fname in FileName:
            if(fname.endswith(ExtensionName)):
                print(fname)
                Data.append(fname)

    CreateLogFile(Data , ExtensionName)

def CreateLogFile(Data , Ename):

    Border = "-"*40
    FileName = "LogFile%s"%(time.ctime())

    fobj = open(FileName , "w")
    fobj.write(Border + "\n")
    fobj.write("--------------- Log File ---------------\n")
    fobj.write(Border + "\n")
    fobj.write(f"File Names With .{Ename} Extension : "+"\n")
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

    DsiplayFileExtension(sys.argv[1] , sys.argv[2]) 


if __name__ == "__main__":
    main()