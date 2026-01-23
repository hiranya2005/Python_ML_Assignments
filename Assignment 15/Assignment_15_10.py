#Q10

CountEven = lambda no : no % 2 == 0


def main():
    
    Data1 = [1,2,3,15,30 , 400]

    fData = len(list(filter(CountEven , Data1)))

    print(fData)


if __name__ == "__main__":
    main()