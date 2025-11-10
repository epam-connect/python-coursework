#Async tasks that can run parerelly
import asyncio

async def fetch_data(delay):
    print("Fetching data....")
    await asyncio.sleep(delay)
    return {"data" : "some data"}


async def main():
    # creates and runs tasks concurrently
    results = await asyncio.gather(fetch_data(2), fetch_data(2), fetch_data(2))     

    print(results)  #collects all results in a list
    

asyncio.run(main())

# Warning
# gather does not care about error handling
# If any task failes other task continues to run leading to undefined behaviour or crash