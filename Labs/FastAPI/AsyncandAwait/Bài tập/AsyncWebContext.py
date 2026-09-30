import asyncio
import time
import re

def parse_data(html):
    match = re.search(r"<h1>(.*?)</h1>", html)
    if match:
        return match.group(1)
    return "Data not found"


async def generate_urls():
    for i in range(1, 5):
        await asyncio.sleep(0.1)
        yield f"http://example.com/page_{i}"


class webConnection:
    def __init__(self, url):
        self.url = url

    async def __aenter__(self):
        print(f"Mở kết nối mạng... ({self.url})")
        await asyncio.sleep(0.5)
        
        # Trích xuất hậu tố URL (ví dụ: "page_1") để tạo dữ liệu HTML động
        page_id = self.url.split("/")[-1]
        
        dynamic_html = f"""
        <!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="UTF-8">
            </head>
            <body>
                <h1>Hello from {page_id}!</h1>
            </body>
        </html>
        """
        return dynamic_html

    async def __aexit__(self, exc_type, exc, tb):
        print(f"Đóng kết nối an toàn ({self.url})")


async def producer(queue):
    async for url in generate_urls():
        print(f"Đưa vào hàng đợi URL {url}")
        await queue.put(url)

    await queue.put(None)
    await queue.put(None)


async def consumer(name, queue):
    while True:
        url = await queue.get()
        if url is None:
            break

        # Dùng async with để tự động kích hoạt __aenter__ và __aexit__
        async with webConnection(url) as html:
            # chaining để gọi hàm xử lý dữ liệu
            extracted_info = parse_data(html)
            print(f"{name} đã trích xuất thành công: {extracted_info}\n")


async def execute():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer("Consumer 1", queue), consumer("Consumer 2", queue))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(execute())
    elapsed = time.perf_counter() - start
    print(f"Execute time: {elapsed:.2f}s")