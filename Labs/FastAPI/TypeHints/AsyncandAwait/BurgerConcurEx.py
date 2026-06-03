from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()
#1. Hàm async cho việc lấy burger, hàm này ở đây sẽ nói cho Python là:
'''
Tác vụ này sẽ có khoảng thời gian chờ đợi,
chuẩn bị thay đổi hướng nếu cần
'''
async def get_burgers(number: int):
    # Giả lập 2 giây đợi cho đến khi nấu xong
    # từ khóa 'await' ở đây sẽ để Python thoát khỏi "vỉ nướng" trong 2 giây đó
    await asyncio.sleep(2)
    return f"{number} Fresh Burgers coming!"


# Hàm async ở đây cho phép "quầy" nhận nhiều thực đơn cùng một lúc
@app.get('/burgers')
async def read_burgers():
    # 'await' thực hiện toán vụ và ngừng thực đơn cụ thể này
    # Khi mà "vỉ nướng" bận 2 giây, Python chạy qua để "phục vụ" cho vị khách thứ hai
    burgers = await get_burgers(2)

    # Khi mà 2 giây đã kết thúc, Python quay trở lại đây để đưa đồ ăn đã nhận:
    return {"message": "Order complete!", "food": burgers}


if __name__ == "__main__":
    uvicorn.run("BurgerConcurEx:app", host="127.0.0.1", port=8000, reload=True)