from multiprocessing import Process
import time

def fun(name):
    print(f"Process : {name} started!")
    time.sleep(5)
    print(f"Process : {name} ended!")

if __name__ == "__main__":
    process_list = []

    for n in ("Ankan", "Rahul", "Sumit"):
        process = Process(
            target=fun,
            args=(n,)
        )
        process.start()
        process_list.append(process)

    for p in process_list:
        p.join()

    print("Main finished")
