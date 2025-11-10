# We can create Future objects ie. Promise of an eventual result
import asyncio

async def solve(future):
    print("Solving Future....")
    await asyncio.sleep(3)
    future.set_result("Future resolved")
    print("Solve completed")

async def cancel(future):
    print("Cancelling future....")
    await asyncio.sleep(3)
    future.cancel()
    print("Cancel completed")


async def main():
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    
    asyncio.create_task(solve(future))

    await future

    print(future.result())

asyncio.run(main())
