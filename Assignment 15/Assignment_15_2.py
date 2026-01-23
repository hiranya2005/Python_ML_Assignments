#Q2

CheckEven = lambda no : no % 2 == 0


def main():
    
    Data = [1 , 2 , 3 ,4, 5]

    fData = list(filter(CheckEven , Data))

    print(fData)


if __name__ == "__main__":
    main()