import asyncio

async def square(n):
    return n * n

async def main():
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i in range(1, 1000 + 1):
            task = tg.create_task(square(i))
            tasks.append(task)
    
    result = [ task.result() for task in tasks ]
    
    for n in result:
        print(n)

asyncio.run(main())