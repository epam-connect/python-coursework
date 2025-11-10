import asyncio

async def waiter(event):
    print("Event is waiting...")
    await event.wait()
    print("Event finished")


async def setter(event):
    await asyncio.sleep(3)
    event.set()
    print("Event has been set..")


async def main():
    event = asyncio.Event()

    await asyncio.gather(waiter(event), setter(event))


asyncio.run(main())