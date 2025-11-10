#Async IO Introduction

import asyncio
import time

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)

    print("Task 2 finished")

async def task3():
    print("Task 3 started")
    await asyncio.sleep(1)
    print("Task 3 finished")


#main is the wrapper function for async functions
async def main():
    await asyncio.gather(task1(), task2(), task3())

asyncio.run(main())
# def sync_task():
#     print("sync_task finished")

# sync_task()