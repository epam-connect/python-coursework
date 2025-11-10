from multiprocessing import Process, Lock
import time

def fun(lock):
    lock.acquire()
    try:
        print("Critical section")
        time.sleep(2)
    finally:
        lock.release()

if __name__ == "__main__":
    lock = Lock()
    Process(
        target= fun,
        args=(lock,)
    ).start()