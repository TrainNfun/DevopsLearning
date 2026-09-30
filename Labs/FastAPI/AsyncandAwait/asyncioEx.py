"""
Như đã biết, coroutine là một đối tượng có thể dừng sự thực thi trong khoảng thời gian nhất định
và sẽ quay lại sau. Trong khoảng thời gian đó, nó có thể đưa sự điều khiển vào vòng lặp sự kiện
mà có thể sử dụng để thực hiện một coroutine khác.

Đối tượng coroutine là kết quả từ việc gọi hàm coroutine, tức là hàm bất đồng bộ, ta định nghĩa một
coroutine với hàm khởi tạo async def
"""

# Ví dụ 1: Dùng module time bình thường
"""
import time
def count():
    print("One")
    time.sleep(1)
    print("Two")
    time.sleep(1)


def counting():
    for _ in range(3):
        count()


if __name__ == "__main__":
    start = time.perf_counter()
    counting()
    elapsed = time.perf_counter() - start
    print(f"Chương trình thực hiện với thời gian là {elapsed:0.2f} giây.")
"""
#Ví dụ 2: Dùng module asyncio
import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    await asyncio.sleep(1)


async def counting():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time
    start = time.perf_counter()
    asyncio.run(counting())
    elapsed = time.perf_counter() - start
    print(f"Chương trình đã thực hiện với thời gian là {elapsed:0.2f} giây.")
