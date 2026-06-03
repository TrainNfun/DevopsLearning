def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello World!")


say_hi("jame".capitalize());

'''
Việc sử dụng str | None thay vì chỉ str sẽ giúp trình soạn thảo phát hiện các lỗi, 
trong đó ta có thể cho rằng một giá trị luôn là kiểu str, 
trong khi thực tế nó cũng có thể là None.
'''