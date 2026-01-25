#Q10

def CountLength(str):
   
    Count = 0
    for i in str:
        Count = Count + 1
    return Count
def main():

    Name = input("Enter name : ")
    iRet = CountLength(Name)
    print(iRet)


if __name__ == "__main__":
    main()