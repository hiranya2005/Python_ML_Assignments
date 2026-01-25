def ChkPrime(no):

    for i in range(2 , no // 2 + 1):
        if no % i == 0:
            return False
    return True
