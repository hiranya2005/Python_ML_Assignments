#Q9

from functools import reduce

DivisibleBy3and5 = lambda no1 , no2 : no1*no2


def main():
    
    Data1 = [1,2,3,15,30]

    rData = reduce(DivisibleBy3and5 , Data1)

    print(rData)


if __name__ == "__main__":
    main()