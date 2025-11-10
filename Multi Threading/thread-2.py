from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
    
    def run(self):
        for i in range(10):
            time.sleep(1)
            print(f"Thread - {self.id}      {i}")

thread1 = MyThread(1, "Ankan Thread")
thread2 = MyThread(2, "Someone Thread")

thread1.start()
thread2.start()

print("Main thread finished")