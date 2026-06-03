const express = require('express');
const app = express();
const PORT = 3000;
//Cho phép Express đọc dữ liệu dưới dạng JSON
app.use(express.json());
//Dữ liệu thử nghiệm
let snacks = [
    { id: 1, prodname: "Mì hảo hảo", price: 6000 },
    { id: 2, prodname: "Sting Energy", price: 10000 },
    { id: 3, prodname: "Oshi Snack", price: 6000 }
];
//1 - GET endpoint - Đọc hết tất cả các đồ ăn vặt
app.get("/api/snacks", (req, res) => {
    res.status(200).json(snacks);
});
//2 - GET endpoint - Đọc một đồ ăn vặt bằng ID
app.get("/api/snacks/:id", (req, res) => {
    const snackId = parseInt(req.params.id);
    const snack = snacks.find(item => item.id === snackId); //Lấy từng đồ ăn vặt với biến item đại diện cho từng id của mỗi sản phẩm.
    if(!snack) {
        return res.status(404).json({message: "Không thấy đồ ăn vặt đó"});
    }
    res.status(200).json(snack);
});
//3 - POST endpoint - Tạo một đồ ăn vặt mới
app.post("/api/snacks", (req, res) => {
    if(!req.body.prodname || !req.body.price) {
        return res.status(400).json({
            message: "Bad request: Cần tên và giá sản phẩm"
        });
    }
    const newSnack = {
        id: snacks.length + 1,
        prodname: req.body.prodname,
        price: req.body.price
    }
    snacks.push(newSnack); //Thêm đồ ăn vặt mới vào vị trí sau cùng
    res.status(201).json({
        message: "Thêm vào một đồ ăn vặt thành công"
    });
});
app.delete("/api/snacks/:id", (req, res) => {
    const snackId = parseInt(req.params.id);
    const initialLength = snacks.length;
    snacks = snacks.filter(item => item.id !== snackId);
    if(snacks.length === initialLength) {
        return res.status(404).json({
            message: "Không thể xóa vì không có đồ ăn vặt đó"
        });
    }
    res.status(200).json({
        message: `Đồ ăn vặt với ID ${snackId} đã được xóa`
    });
});
app.listen(PORT, () => {
    console.log(`REST API demo đồ ăn vặt hiện tại đang dựng tại địa chỉ http://localhost:${PORT}`);
});