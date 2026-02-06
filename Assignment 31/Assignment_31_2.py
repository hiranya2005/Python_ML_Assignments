import os
import sys
import time

def ReplaceFileExtension(DirectoryName , ExtensionName1 , ExtensionName2):

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
            if(fname.endswith(ExtensionName1)):
                old_path = os.path.join(FolderName, fname)
                new_name = fname.replace(ExtensionName1, ExtensionName2)
                new_path = os.path.join(FolderName, new_name)
                os.rename(old_path, new_path)
                Data.append(new_name)

    CreateLogFile(Data , ExtensionName2)

def CreateLogFile(Data , Ename):

    Border = "-"*40
    FileName = "LogFile%s"%(time.ctime())

    fobj = open(FileName , "w")
    fobj.write(Border + "\n")
    fobj.write("--------------- Log File ---------------\n")
    fobj.write(Border + "\n")
    fobj.write(f"File Names With replaced {Ename} Extension : "+"\n")
    for name in Data:
        fobj.write(name + "\n")

    fobj.write(Border + "\n")
    fobj.write("--------------- Log File ---------------\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():

    if len(sys.argv) != 4:
        print("Invalid Number of Arguments...")
        return

    sys.argv[1] = os.path.abspath(sys.argv[1])

    print(sys.argv[1])

    ReplaceFileExtension(sys.argv[1] , sys.argv[2] ,sys.argv[3]) 


if __name__ == "__main__":
    main()