#Q1

ReturnSquare = lambda no : no * no


def main():
    
    Data = [1 , 2 , 3 ,4, 5]

    mData = list(map(ReturnSquare , Data))

    print(mData)


if __name__ == "__main__":
    main()