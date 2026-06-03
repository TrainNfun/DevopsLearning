# Ví dụ gợi ý kiểu theo việc sử dụng kiểu list chuỗi
def process_items(items: list[str]):
    for item in items:
        print(item) # Đặt một dấu chấm rồi thử dùng autocomplete để xem các hàm dành cho chuỗi


process_items(["1", "2", "3", "4"])
process_items(["John", "James", "Jane", "Jose"])

# Ví dụ gợi ý kiểu theo tuple và set
def process_items2(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s # Đặt một dấu chấm rồi thử dùng autocomplete để xem các hàm dành các kiểu


res = process_items2((1, 2, "String"), {3, 4, "\x48\x65\x6c\x6c\x6f"})
print(res)

'''
Tức là:
    Biến items_t là một tuple với 3 item lần lượt các kiểu là int và str.
    Biến item_s là một set với mỗi item bên trong là kiểu bytes
'''

# Ví dụ gợi ý kiểu theo dictionary
def process_items3(prices: dict[str, float]):
    for item_name, item_price in prices.items(): #Dùng dấu chấm tại tham số biến prices rồi xem các hàm dành cho dict
        print(item_name)
        print(item_price)


process_items3({"Fish": 5.6})
process_items3({"Meat": 7.8})