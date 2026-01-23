#Q8

DivisibleBy3and5 = lambda no  : no % 3 == 0 and no % 5 == 0


def main():
    
    Data1 = [1,2,3,15,30]

    fData = list(filter(DivisibleBy3and5 , Data1))

    print(fData)


if __name__ == "__main__":
    main()