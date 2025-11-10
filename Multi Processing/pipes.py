from multiprocessing import Process, Pipe
import time

def fun(child_con):
    time.sleep(5)
    child_con.send("Hello parent")
    child_con.close()


if __name__ == "__main__":
    parent_con, child_con = Pipe()

    process = Process(
        target=fun,
        args=(child_con,)
    )
    process.start()

    print(parent_con.recv())
    process.join()