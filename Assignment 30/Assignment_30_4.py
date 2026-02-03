import os

def DisplayLineByLine(OldFile , NewFile):
    
    Ret = os.path.exists(OldFile)
    if Ret == False:
        print("File does not exists")
        return
    
    Ret = os.path.isdir(OldFile)
    if Ret == True:
        print("Please enter file name")
        return
    
    ofobj = open(OldFile , "r")
    nfobj = open(NewFile , "w")

    Buffer = ofobj.read(100)
    while(len(Buffer) > 0):

        nfobj.write(Buffer)
        Buffer = ofobj.read(100)

    print(f"{OldFile} content copied inside {NewFile} Successfully...")
    
    ofobj.close()
    nfobj.close()

def main():
    
    Fname = input("Enter the name of Existing file : ")
    Fname1 = input("Enter the name of new file : ")
    DisplayLineByLine(Fname , Fname1)

if __name__ == "__main__":
    main()