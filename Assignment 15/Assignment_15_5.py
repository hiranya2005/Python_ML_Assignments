#Q5

from functools import reduce

ReturnMaximum = lambda no1 , no2 : no1 if no1 > no2 else no2


def main():
    
    Data = [1 , 2 , 3 ,4, 5]

    rData = reduce(ReturnMaximum , Data)

    print(rData)


if __name__ == "__main__":
    main()