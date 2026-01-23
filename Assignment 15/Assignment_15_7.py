#Q7
#Wrong Ans
CheckGreaterThan5 = lambda no1 , no2 : no1


def main():
    
    Data1 = ['h' , 'e' , 'e' , 'l' , 'l' , '0']
    Data2 = ['h' , 'e' , 'e' , 'l']

    fData = list(filter(CheckGreaterThan5 , Data1 , Data2))

    print(fData)


if __name__ == "__main__":
    main()