import queue
from threading import Thread
import time

q = queue.Queue(maxsize=5)

def produce(number):
    for i in range(10):
        time.sleep(1)
        q.put(i)
        print(f"Produced{number} item : {i}")
        # q.task_done()

def consume():
    for i in range(20):
        time.sleep(1)
        item = q.get()
        print(f"Consumed item : {item}")
        q.task_done()

producer_thread = Thread(target=produce, args=(1,))
producer_thread1 = Thread(target=produce, args=(2,))
consumer_thread = Thread(target=consume)

producer_thread.start()
producer_thread1.start()
consumer_thread.start()

producer_thread.join()
producer_thread1.join()
consumer_thread.join()