#Spawn 50 processes for 1 to 50, and cube each no. in incremental order using Queu

from multiprocessing import Process
from multiprocessing import Queue, Lock


def add_cube(i, q, lock):
    lock.acquire()
    q.put(i**3)
    lock.release()

process_list = []

if __name__ == "__main__":
    q = Queue(50)
    lock = Lock()
    for i in range(1, 50 + 1):
        p = Process(target=add_cube, args=(i, q, lock))
        process_list.append(p)
        p.start()

    print("Main Process is waiting....")
    for p in process_list:
        p.join()

    while not q.empty():
        print(q.get())