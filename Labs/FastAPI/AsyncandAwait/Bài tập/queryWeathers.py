import asyncio
import time
import random

async def weatherA():
    print(f"Querying weather A")
    delay1 = random.uniform(1, 3)
    await asyncio.sleep(delay1)
    print(f"Successfully querying weather A")


async def weatherB():
    print(f"Querying weather B")
    delay2 = random.uniform(0.5, 2)
    await asyncio.sleep(delay2)
    print(f"Successfully querying weather B")


async def weatherC():
    print(f"Querying weather C")
    delay3 = random.uniform(2, 4)
    await asyncio.sleep(delay3)
    print(f"Successfully querying weather C")


async def execute():
    await asyncio.gather(weatherA(), weatherB(), weatherC())


if __name__ == "__main__":
    random.seed(444)
    start = time.perf_counter()
    asyncio.run(execute())
    elapsed = time.perf_counter() - start
    print(f"Execute time: {elapsed:.2f}s")