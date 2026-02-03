import os

def CheckFile(Fname):

    Ret = os.path.exists(Fname)
    if Ret == True:
        print(f"{Fname} Exists")
    else:
        print(f"{Fname} Does not exists")

def main():
    
    FileName = input("Enter File Name : ")
    CheckFile(FileName)

if __name__ == "__main__":
    main()