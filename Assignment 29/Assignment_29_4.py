import sys
import os
import hashlib

def CheckFileContent(FileName1 , FileName2):
    
    Ret1 = os.path.exists(FileName1)
    Ret2 = os.path.exists(FileName2)

    if Ret1 == False or Ret2 == False:
        if Ret1 == False:
            print(f"{FileName1} does not exists")
        else:
            print(f"{FileName2} does not exists...")
        return
    
    fobj1 = open(FileName1 , "rb")
    hobj1 = hashlib.md5()

    Buffer = fobj1.read(100)

    while(len(Buffer) > 0):
        hobj1.update(Buffer)
        Buffer = fobj1.read(100)

    CheckSum1 = hobj1.hexdigest()
    fobj1.close()
    
    fobj2 = open(FileName2 , "rb")
    hobj2 = hashlib.md5()

    Buffer = fobj2.read(100)

    while(len(Buffer) > 0):
        hobj2.update(Buffer)
        Buffer = fobj2.read(100)

    CheckSum2 = hobj2.hexdigest()
    fobj2.close()
    
    if(CheckSum1 == CheckSum2):
        return True
    else:
        return False
        

def main():
   
   if len(sys.argv) != 3: 
       print("File Names must be two...")

   Ret = CheckFileContent(sys.argv[1] , sys.argv[2])

   if Ret == True:
       print("Success")
   else:
       print("Failure")


if __name__ == "__main__":
    main()