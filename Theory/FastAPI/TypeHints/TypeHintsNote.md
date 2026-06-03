# Gợi ý kiểu trên Python

Python hỗ trợ các "gợi ý kiểu" (type hints) tùy chọn (còn được gọi là "chú thích kiểu" - type annotations).

Những chú thích kiểu đó là những cú pháp đặc biệt cho phép khai báo một kiểu của biến. Nó giúp việc sử dụng autocompletion trong editor dễ dàng hơn với các phương thức hay sử dụng.

Các ví dụ bao gồm typehintsEx1.py.

## Khai báo kiểu trên Python

### Các kiểu đơn giản

Ta có thể sử dụng gợi ý kiểu trên tất cả các kiểu tiêu chuẩn của Python, ví dụ như:

+ `int`
+ `float`
+ `bool`
+ `bytes`

Trong trường hợp đặc biệt mà ta cần khai báo một biến cho phép sử dụng tất cả các kiểu dữ liệu, ta có thể sử dụng thư viện `Any` từ module `typing`. Xem ví dụ tại typingmoduleEx.py.

### Các kiểu thông thường

Một số kiểu dữ liệu có thể nhận "tham số kiểu" (type parameters) trong dấu ngoặc vuông để định nghĩa kiểu bên trong của chúng, ví dụ như danh sách chuỗi sẽ được khai báo là `list[str]`.

Những kiểu dữ liệu có thể nhận tham số kiểu này gọi là kiểu chung (Generic types) hay kiểu tổng quát (Generics).

Ta có thể sử dụng các kiểu dữ liệu tích hợp sẵn tương tự như kiểu tổng quát (với dấu ngoặc vuông và kiểu bên trong) như sau:

+ `list`
+ `tuple`
+ `set`
+ `dict`

Lưu ý ở kiểu `dict`, ta cần truyền 2 tham số kiểu cho nó và cách nhau bởi dấu phẩy như sau:

+ Tham số kiểu đầu tiên là khóa (key).
+ Tham số kiểu thứ hai là giá trị (value).

Các ví dụ bao gồm typehintsEx2.py.

### Union

Có thể khai báo các biến với nhiều kiểu dữ liệu (ví dụ như `int` hay `str`). Để định nghĩa như thế ta sử dụng dấu gạch ngang (| - phép OR) để phân cách hai kiểu dữ liệu. Đây được gọi là "hợp" (union) vì biến có thể thuộc bất kỳ kiểu dữ liệu nào trong tập hợp của hai kiểu dữ liệu đó.

Ví dụ được thực hiện tại typehintsEx3.py

### None

Ta có thể sử dụng kiểu `None`, là một kiểu dữ liệu để định nghĩa một giá trị null hoặc không có giá trị nào.

Ví dụ được thực hiện tại typehintsEx4.py

### Các lớp như các kiểu

Ta cũng có thể khai báo một lớp như là một kiểu của một biến. Hãy cho ví dụ như là một lơp Person với một tên:

```
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name
```

Và ta cũng sẽ nhận được sự hỗ trợ của autocomplete editor. Với ý nghĩa là "`one_person` là một thể hiện của lớp `Person`" (không có nghĩa là `one_person` là lớp `Person`).

Có thể tham khảo ví dụ tại typehintsClassEx.py.

## Pydantic

Pydantic là một thư viện của Python để thực hiện xác thực dữ liệu. Ta có thể khai báo một "hình thù" của một dữ liệu như các lớp với các thuộc tính, mỗi thuộc tính sẽ có một kiểu. Sau đó ta tạo ra một thể hiện từ một lớp đó với một số giá trị và nó sẽ xác thực các giá trị đó và chuyển về kiểu phù hợp (nếu cần) và cho ta một đối tượng với tất cả các dữ liệu. Ta cũng được sự hỗ trợ từ autocomplete với đối tượng thu được từ kết quả.

Hiểu đơn giản Pydantic như là một người bảo vệ cho dữ liệu ứng dụng của ta. Bây giờ nếu ở Python bình thường. Ta mong rằng tuổi của một người dùng là một số nguyên dương, nhưng có ai đó lại truyền thành chuỗi như "eighteen" hoặc số âm như -10, Python sẽ không quan tâm và phàn nàn gì cho đến khi code của ta bị crash hoặc lỗi trầm trọng. Pydantic giải quyết vấn đề này bằng việc sử dụng gợi ý kiểu thông thường để tự động xác thực, làm sạch và chuyển đổi dữ liệu tại thời gian chạy.

Để hiểu hơn về ví dụ, tham khảo tại typehintsPydanticEx.py.

## Gợi ý kiểu trong FastAPI

FastAPI lợi dụng các điểm mạnh của việc gợi ý kiểu để thực hiện nhiều thứ.

Với FastAPI ta có thể khai báo các tham số với các gợi ý kiểu và ta sẽ nhận được:

+ Sự hỗ trợ của editor.
+ Kiểm tra kiểu.

và FastAPI sử dụng các khai báo đó để:

+ Định nghĩa các yêu cầu: Từ các tham số đường dẫn yêu cầu, tham số truy vấn, các tiêu đề, các thân, các phần phụ thuộc, v.v.
+ Chuyển đổi dữ liệu từ yêu cầu trở thành kiểu cần được có.
+ Xác thực dữ liệu đến từ các yêu cầu và tạo thông báo lỗi tự động trả về cho máy khách nếu dữ liệu là không hợp lệ.
+ Ghi lại API sử dụng OpenAPI mà thông tin này được sử dụng bởi giao diện người dùng tài liệu tương tác tự động.
