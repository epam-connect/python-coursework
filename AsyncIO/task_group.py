#Usage of TaskGroup that efficiently manages all tasks with proper Error Handling
import asyncio

async def fetch_data(delay):
    print("Fetching data....")
    await asyncio.sleep(delay)
    return {"data" : "some data"}

async def main():
    tasks = []

    async with asyncio.TaskGroup() as tg:               #task context manager
        for _, delay in enumerate([2, 3, 5]):
            task = tg.create_task(fetch_data(delay))
            tasks.append(task)

    result = [ task.result() for task in tasks ]
    print(result)

asyncio.run(main())

# from collections import Counter, defaultdict, deque
# import heapq

# q = deque()