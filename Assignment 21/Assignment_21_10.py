import threading

sum_result = 0
product_result = 1


def calculate_sum(numbers):
    global sum_result
    total = 0
    for num in numbers:
        total += num
    sum_result = total


def calculate_product(numbers):
    global product_result
    prod = 1
    for num in numbers:
        prod *= num
    product_result = prod

n = int(input("Enter number of elements: "))
values = []

print("Enter elements:")
for i in range(n):
    values.append(int(input()))


t1 = threading.Thread(target=calculate_sum, args=(values,), name="SumThread")
t2 = threading.Thread(target=calculate_product, args=(values,), name="ProductThread")


t1.start()
t2.start()


t1.join()
t2.join()


print("Sum of elements:", sum_result)
print("Product of elements:", product_result)
print("Exit from main")