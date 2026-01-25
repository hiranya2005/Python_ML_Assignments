import threading


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_list(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)

    print("Thread Name:", threading.current_thread().name)
    print("Prime numbers:", primes)
    print("---------------------------")

def nonprime_list(numbers):
    nonprimes = []
    for num in numbers:
        if not is_prime(num):
            nonprimes.append(num)

    print("Thread Name:", threading.current_thread().name)
    print("Non-prime numbers:", nonprimes)
    print("---------------------------")

n = int(input("Enter number of elements: "))
values = []

print("Enter elements:")
for i in range(n):
    values.append(int(input()))


t1 = threading.Thread(target=prime_list, args=(values,), name="Prime")
t2 = threading.Thread(target=nonprime_list, args=(values,), name="NonPrime")


t1.start()
t2.start()


t1.join()
t2.join()

print("Exit from main")