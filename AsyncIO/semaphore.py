import asyncio

semaphore = asyncio.Semaphore(2)


async def modify(id):

    async with semaphore:
        print(f"Task {id} modifying..")
        await asyncio.sleep(2)


async def main():
    await asyncio.gather(* (modify(i) for i in range(5)) )

asyncio.run(main())