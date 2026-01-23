#Q3

CheckOdd = lambda no : no % 2 != 0


def main():
    
    Data = [1 , 2 , 3 ,4, 5]

    fData = list(filter(CheckOdd , Data))

    print(fData)


if __name__ == "__main__":
    main()