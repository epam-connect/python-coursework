import asyncio

lock = asyncio.Lock()

count = 0

async def increase():
    global count

    async with lock:
        print("Resource before modification", count)
        await asyncio.sleep(2)
        count += 1
        print("Resource after modification", count)



async def main():
    await asyncio.gather(* (increase() for _ in range(5)) )

asyncio.run(main())