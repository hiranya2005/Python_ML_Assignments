import sys
import os
def CopyFile(OldFile):
    
    Value = 0
    Ret = os.path.exists(OldFile)
    if Ret == False:
        print("File Does not Exist...")
        return
    
    ofobj = open(OldFile , "r")

    nfobj = open("Demo.txt" , "w")

    Buffer = ofobj.read(100)
    while(len(Buffer) > 0):
        iRet = nfobj.write(Buffer)
        Value = Value + iRet
        Buffer = ofobj.read(100)

    print("New File Created Successfully")
    print("Bytes copied : ", Value)
    
    nfobj.close()
    ofobj.close()

def main():

    CopyFile(sys.argv[1])

if __name__ == "__main__":
    main()