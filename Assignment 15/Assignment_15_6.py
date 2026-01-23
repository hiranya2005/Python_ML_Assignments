#Q6

from functools import reduce

ReturnMinimum = lambda no1 , no2 : no1 if no1 < no2 else no2


def main():
    
    Data = [1 , 2 , 3 ,4, 5]

    rData = reduce(ReturnMinimum , Data)

    print(rData)


if __name__ == "__main__":
    main()