import threading


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    print("Thread Name:", threading.current_thread().name)
    print("Maximum element:", maximum)
    print("---------------------------")

def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    print("Thread Name:", threading.current_thread().name)
    print("Minimum element:", minimum)
    print("---------------------------")


n = int(input("Enter number of elements: "))
values = []

print("Enter elements:")
for i in range(n):
    values.append(int(input()))


t1 = threading.Thread(target=find_max, args=(values,), name="MaxThread")
t2 = threading.Thread(target=find_min, args=(values,), name="MinThread")


t1.start()
t2.start()


t1.join()
t2.join()

print("Exit from main")