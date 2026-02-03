def DisplayFileContent(FileName):

    fobj = open(FileName , "r")

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        print(Buffer , end=" ")
        Buffer = fobj.read(1024)

    

def main():
    Fname = input("Enter File Name : ") 
    DisplayFileContent(Fname)

if __name__ == "__main__":
    main()