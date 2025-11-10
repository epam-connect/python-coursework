import threading
import time

def fun():
    print("Child Thread starts")
    print(threading.current_thread().name)
    for i in range(10):
        time.sleep(1)
        print(i)
    print("Child Thread finished")

thread = threading.Thread(
    target= fun
)


print("Main thread waiting")
print(threading.current_thread().name)
thread.start()
thread.join()
print("Main thread finished")