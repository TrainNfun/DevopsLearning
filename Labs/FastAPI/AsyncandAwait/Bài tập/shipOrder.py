import asyncio
import time

async def prepare_order(order_id):
    print(f"Preparing food order: {order_id}")
    await asyncio.sleep(1.5)
    orders = {"id": order_id, "name": f"Order {order_id}"}
    print(f"Prepared food order: {order_id}")
    return orders


async def deliver_order(orders):
    print(f"Receiving {orders['name']}")
    await asyncio.sleep(1)
    print(f"Deliver {orders['name']}")


async def ship_order(order_id):
    orders = await prepare_order(order_id)
    await deliver_order(orders)


async def execute():
    order_ids = [101, 102, 103]
    await asyncio.gather(*(ship_order(order_id) for order_id in order_ids))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(execute())
    elapsed = time.perf_counter() - start
    print(f"Execute time: {elapsed:.2f}s")