from multiprocessing import Process, Value, Array
import time

def fun(val, arr):
    val.value = 3

    for i in range(len(arr)):
        arr[i] = -arr[i]


if __name__ == "__main__":
    val = Value('i', 1)
    arr = Array('i', [1, 2,3,4])
    p = Process(
        target=fun,
        args=(val, arr)
    )

    p.start()
    p.join()

    print(val.value)
    for n in arr:
        print(n)