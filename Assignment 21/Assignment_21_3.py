import threading

counter = 0

lock = threading.Lock()


def increment_counter(times):
    global counter
    for i in range(times):
        lock.acquire()
        counter += 1
        lock.release()


t1 = threading.Thread(target=increment_counter, args=(10000,), name="Thread1")
t2 = threading.Thread(target=increment_counter, args=(10000,), name="Thread2")
t3 = threading.Thread(target=increment_counter, args=(10000,), name="Thread3")


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


print("Final value of counter:", counter)