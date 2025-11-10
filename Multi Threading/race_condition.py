import threading
import time

count = 0
def increase():
    global count
    for i in range(2000):
        # time.sleep(0.5)
        count += 1
        print(f"{threading.current_thread().name}  to {count}")

def decrease():
    global count
    for i in range(1000):
        # time.sleep(0.5)
        count -= 1
        print(f"{threading.current_thread().name}  to {count}")

thread1 = threading.Thread(
    target= increase
)
thread2 = threading.Thread(
    target= decrease
)

thread1.start()
thread2.start()