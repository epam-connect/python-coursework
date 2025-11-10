#Async tasks that can run parerelly
import asyncio

async def fetch_data(delay):
    print("Fetching data....")
    await asyncio.sleep(delay)
    return {"data" : "some data"}


async def main():
    task1 = asyncio.create_task(fetch_data(2))  # task1 - Coroutine object
    task3 = asyncio.create_task(fetch_data(2))  # task2 - Coroutine object
    
    result1 = await task1   #will start immediately
    print(result1)

    task2 = asyncio.create_task(fetch_data(2))  # task2 - Coroutine object

    result2 = await task2   #will start immediately
    print(task2.result())   #task2.result() also gives the result
    
    result3 = await task3   #will start immediately
    print(result3)
    

asyncio.run(main())