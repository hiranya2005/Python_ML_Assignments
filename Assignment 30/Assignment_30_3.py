import os
import time
def DisplayLineByLine(FileName):
    
    Ret = os.path.exists(FileName)
    if Ret == False:
        print("File does not exists")
        return
    
    Ret = os.path.isdir(FileName)
    if Ret == True:
        print("Please enter file name")
        return
    
    fobj = open(FileName , "r")

    Buffer = fobj.readlines()

    for i in range(len(Buffer)):
        print(Buffer[i])
        time.sleep(1)
        
    fobj.close()    

def main():
    
    Fname = input("Enter the name of file : ")
    DisplayLineByLine(Fname)

if __name__ == "__main__":
    main()