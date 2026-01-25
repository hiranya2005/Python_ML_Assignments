import threading


def display_forward():
    print("Thread1 started")
    for i in range(1, 51):
        print(i)
    print("Thread1 completed")

def display_reverse():
    print("Thread2 started")
    for i in range(50, 0, -1):
        print(i)
    print("Thread2 completed")

t1 = threading.Thread(target=display_forward, name="Thread1")
t2 = threading.Thread(target=display_reverse, name="Thread2")


t1.start()
t1.join()


t2.start()
t2.join()

print("Exit from main thread")