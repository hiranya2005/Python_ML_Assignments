#Q4

from functools import reduce

AddElements = lambda no1 , no2 : no1 + no2


def main():
    
    Data = [1 , 2 , 3 ,4, 5]

    rData = reduce(AddElements , Data)

    print(rData)


if __name__ == "__main__":
    main()