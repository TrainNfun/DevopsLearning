from pydantic import BaseModel, Field, EmailStr, ValidationError

class userRegistration(BaseModel):
    # trường ID, bắt buộc, phải là số nguyên
    user_id: int

    # trường văn bản với độ dài xác thực
    username: str = Field(min_length=3, max_length=20)

    # kiểu Pydantic đặc biệt kiểm tra tự động định dạng email
    email: EmailStr

    # trường số với các vùng xác thực (lớn hơn hoặc bằng 18 và bé hơn hoặc bằng 80)
    age: int = Field(ge=18, le=80)

    # trường tự chọn với giá trị mặc định
    is_premium: bool = False

# Bỏ dấu comment multiline ra để làm
'''
# Trường hợp đầu tiên là cho dữ liệu tốt (ép buộc dữ liệu - data coercion)
good_data = {
    "user_id": "101", #để ý ở đây không là kiểu int
    "username": "tester",
    "email": "foo@gmail.com",
    "age": 25 
}
user = userRegistration(**good_data)

print(user.username) # tester
print(type(user.user_id)) # nếu là <class 'int'> thì Pydantic đã chuyển đổi an toàn dữ liệu chuỗi "101" thành 101
print(user.is_premium) # sử dụng giá trị mặc định là False
'''

# Trường hợp thứ hai là cho dữ liệu xấu (thực hiện xác thực)
bad_data = {
    "user_id": "not-a-number", # không thể đổi thành số nguyên
    "username": "jo", # ngắn quá, độ dài tối thiểu là 3
    "email": "invalid-email.com", # thiếu dấu @ và cấu trúc hợp lệ
    "age": 12 # quá trẻ (dưới 18 tuổi)
}
try:
    invalid_user = userRegistration(**bad_data)
except ValidationError as e:
    print(e) # ở đây, nó sẽ báo lỗi cụ thể là từng cặp khóa - giá trị bên trong bị vấn đề gì và cách khắc phục

# Bây giờ hiểu sơ bộ cụ thể từng thư viện là như sau:
'''
1. BaseModel là MỘT LỚP CƠ SỞ để TẠO MÔ HÌNH Pydantic.
Khi mà tạo một lớp kế thừa từ BaseModel. Python sẽ tiêm động một loạt các công cụ (phương thức và thuộc tính) vào trong lớp thừa kế đó.
2. Field cho phép ta cụ thể hóa kiểu dữ liệu các thuộc tính với các luật (chuỗi phải hợp lệ, độ dài phải phù hợp, giá trị phải không bé hơn,...)
3. EmailStr là một công cụ xác thực email chuyên biệt để xác thực một địa chỉ email.
4. ValidationError sẽ thông báo lỗi từ ba thư viện trên nếu có sự sai phạm trong lúc xác thực.
'''