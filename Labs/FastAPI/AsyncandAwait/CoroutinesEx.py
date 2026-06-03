import asyncio

# Hàm bất đồng bộ này định nghĩa hàm Coroutine (như một blueprint)
async def cook_burger(id):
    print(f"Bắt đầu nấu burger #{id}")
    await asyncio.sleep(2)
    print(f"Hoàn thành burger #{id}")
    return f"Burger #{id}"


async def main():
    # Gọi hàm bất đồng bộ sẽ không chạy mã, nó chỉ tạo ra đối tượng coroutine
    my_coroutine = cook_burger(42)

    print(f"Kiểu của biến là: {type(my_coroutine)}")
    print(f"Đối tượng thật là: {my_coroutine}\n")

    # để thực thi đoạn mã bên trong nó, ta phải đợi nó
    result = await my_coroutine
    print(f"Kết quả trả về: {result}")

# Khởi động vòng lặp sự kiện để chạy khối hàm main()
asyncio.run(main())