#Q1

def Add(no1 , no2):
    return no1+no2

def Sub(no1 , no2):
    return no1-no2

def Multiplication(no1 , no2):
    return no1*no2

def Division(no1 , no2):

    try:
        Result = no1/no2
        return Result
    except ZeroDivisionError as zobj:
        print(zobj)
