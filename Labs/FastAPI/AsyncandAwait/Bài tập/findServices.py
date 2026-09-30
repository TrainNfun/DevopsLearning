import asyncio as aio
import time

async def check_service(name, delay, is_error = False):
    print(f"Scan for service {name}")
    await aio.sleep(delay)
    if is_error:
        raise ConnectionError(f"Can't connect to {name}")
    return f"{name}: 200 OK"


async def execute():
    results = await aio.gather(
        check_service("Database", 1),
        check_service("Cache_Server", 1),
        check_service("Payment_Gateway", 1.5, is_error=True),
        return_exceptions=True
    )

    for result in results:
        if isinstance(result, Exception):
            print(f"Caught exception: {result}")
        else:
            print(result)


if __name__ == "__main__":
    start = time.perf_counter()
    aio.run(execute())
    elapsed = time.perf_counter() - start
    print(f"Execute time: {elapsed:.2f}s")