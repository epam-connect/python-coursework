# asynchronou tasks that does not run parerelly

import asyncio

async def fetch_data(delay):
    print("Fetching data....")
    await asyncio.sleep(delay)
    return {"data" : "some data"}


async def main():
    task1 = fetch_data(2)  # task1 - Coroutine object
    task2 = fetch_data(2)  # task2 - Coroutine object
    task3 = fetch_data(3)  # task2 - Coroutine object
    
    result1 = await task1
    print(result1)
    
    result2 = await task2
    print(result2)

    
    result3 = await task3   # will not start untill task1 finishes
    print(result3)
    

asyncio.run(main())