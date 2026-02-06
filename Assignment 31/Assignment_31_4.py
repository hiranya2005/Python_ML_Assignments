import os
import sys
import time
import shutil

def DirectoryCopyExtension(DirectoryName , NewDirectory , ExtensioName):

    Ret = os.path.exists(DirectoryName)
    if Ret == False:
        print("Directory Does not exists...")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if Ret == False:
        print("ERROR : Enter a valid Directory name")

    Ret = os.path.exists(NewDirectory)
    if Ret == True:
        print("Directory already exists...")
        return

    os.mkdir(NewDirectory)

    Files = os.listdir(DirectoryName)

    Data = list()

    for fname in Files:

        if fname.endswith(ExtensioName):
            Data.append(fname)
            shutil.copy2(os.path.join(DirectoryName , fname) , NewDirectory)

    CreateLogFile(Data , ExtensioName , NewDirectory)

def CreateLogFile(Data , Ename , nDirectory):

    Border = "-"*40
    FileName = "LogFile%s"%(time.ctime())

    fobj = open(FileName , "w")
    fobj.write(Border + "\n")
    fobj.write("--------------- Log File ---------------\n")
    fobj.write(Border + "\n")
    fobj.write(f"Below File Copied with Extension {Ename} Successfully in {nDirectory} : "+"\n")
    for name in Data:
        fobj.write(name + "\n")

    fobj.write(Border + "\n")
    fobj.write("--------------- Log File ---------------\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():

    if len(sys.argv) == 4:
        DirectoryCopyExtension(sys.argv[1] , sys.argv[2] , sys.argv[3]) 
    else:
        print("Invalid Number of Arguments...")
        return


if __name__ == "__main__":
    main()