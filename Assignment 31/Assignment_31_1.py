# Without Directly using endswith fucntion on FileName
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
        return
    
    if ExtensionName.endswith('.'): 
        print("Enter a Valid Extension!")
        return

    if ExtensionName.startswith('.'):
        ExtensionName = ExtensionName.split('.')
        ExtensionName = ExtensionName[len(ExtensionName) - 1]

    Data = list()
    fData = list()

    for FolderName , SubFolderName , FileName in os.walk(DirectoryName):
        
        for fname in FileName:
            Data.append(fname)

    for i in range(len(Data)):

        sData = Data[i].split('.')

        if(len(sData) > 2) and ExtensionName == sData[len(sData) - 1]:
            print(Data[i]) 
            fData.append(Data[i])
        
        if len(sData) == 2:   
            if sData[1] == ExtensionName:
                print(Data[i])
                fData.append(Data[i])
    
    CreateLogFile(fData , ExtensionName)

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