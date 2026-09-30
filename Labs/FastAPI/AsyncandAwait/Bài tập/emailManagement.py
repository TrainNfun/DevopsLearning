import asyncio
import time

async def execute():
    queue = asyncio.Queue()
    email_ids = [1, 2, 3, 4, 5]
    await asyncio.gather(producer(queue, email_ids), consumer1(queue), consumer2(queue))

async def producer(queue, email_ids):
    for email_id in range(1, len(email_ids) + 1):
            print(f"Fetching email_{email_id}")
            print(f"Fetched email_{email_id}")
            await asyncio.sleep(0.2)
            email = {"id": email_id, "name": f"email_{email_id}"}
            await queue.put(email)

    await queue.put(None)
    await queue.put(None)


async def consumer1(queue):
    while True:
        email = await queue.get()
        if email is None:
            break
        print(f"Consumer 1 retrives {email['name']}.")
        await asyncio.sleep(1)
        print(f"Consumer 1 sends {email['name']}.")


async def consumer2(queue):
    while True:
        email = await queue.get()
        if email is None:
            break
        print(f"Consumer 2 retrives {email['name']}.")
        await asyncio.sleep(1)
        print(f"Consumer 2 sends {email['name']}.")


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(execute())
    elapsed = time.perf_counter() - start
    print(f"Execute time: {elapsed:.2f}s")