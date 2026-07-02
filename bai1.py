# code đã sửa
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Laptop Dell", "price": 15000000},
    {"id": 2, "name": "Chuột Logitech", "price": 350000},
    {"id": 3, "name": "Bàn phím cơ", "price": 1200000}
]
@app.get("/products/{product_id}")
def get_product_detail(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "message": "Không tìm thấy sản phẩm"
    }

# Khi gọi GET /products/1, API trả về 404 Not Found vì truyền sai tham số path parameter nên dẫn đến đường URL sai khi muốn truy cập
# dòng code đang khai báo sai path parameter là : @app.get("/products/product_id")
# @app.get("/products/product_id") không phải là path parameter vì thiếu dấu {} nên nó chỉ được coi là 1 URL 
# endpoint đúng cần sửa thành : @app.get("/products/{product_id}")
