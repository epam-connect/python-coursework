from multiprocessing import Process, Queue
import time

def fun(numbers, q):
    time.sleep(2)
    for i in numbers:
        if i % 2 == 0:
            q.put(i)


if __name__ == "__main__":
    q = Queue()
    p = Process(
        target=fun,
        args=(range(1, 11), q)
    )
    p.start()
    p.join()
    
    while not q.empty() :
        print(q.get())