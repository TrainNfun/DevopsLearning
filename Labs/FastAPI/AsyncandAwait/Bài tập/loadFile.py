import asyncio
import time

# đọc rồi tải tệp về, khoảng 2.0000x giây, như ta mong đợi.
async def loadFile(fileName):
    print(f"Load file {fileName}")
    await asyncio.sleep(2)


async def execute():
    await asyncio.gather(loadFile("A"), loadFile("B"), loadFile("C"))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(execute())
    elapsed = time.perf_counter() - start
    print(f"Execute time: {elapsed:.2f}s")