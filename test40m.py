products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def display_products():
    if len(products) == 0:
        print("Danh sách sản phẩm hiện trống")
    else:
        print("--- DANH SÁCH SẢN PHẨM ---")
        print(f"ID  | Tên sản phẩm         | Giá bán")
        print("-------------------------------------------")
        for i in range(len(products)):
            print(f"{products[i].get("id"):<3} | {products[i].get("name"):<20} | {products[i].get("price"):<10}")
        print("-------------------------------------------")

def add_product():
    print("--- THÊM SẢN PHẨM MỚI ---")
    while True:
        id_input = input("Nhập mã sản phẩm: ")
        if id_input == "":
            print("Không được phép để trống!")
            continue
        break

    while True:
        name_input = input("Nhập tên sản phẩm: ")
        if name_input == "":
            print("Không được phép để trống!")
            continue
        break
    
    while True:
        price_input = input("Nhập giá bán: ")
        if price_input == "":
            print("Không được phép để trống!")
            continue
        break

    products.append({'id': id_input, 'name': name_input, 'price': price_input})
    print("Thêm sản phẩm thành công!")

def update_price():
    print("--- CẬP NHẬT GIÁ SẢN PHẨM ---")
    while True:
        id_edit = input("Nhập mã sản phẩm cần sửa giá: ").strip().upper()
        if id_edit == "":
            print("Không được phép để trống!")
            continue
        break

    for i in range(len(products)):
        if id_edit == products[i].get("id"):
            print(f"Tìm thấy sản phẩm: {products[i].get("name")} (Giá hiện tại: {products[i].get("price")})")
            while True:
                new_price = input("Nhập giá mới: ")
                if new_price == "":
                    print("Không được phép để trống!")
                    continue

                break
            products[i]["price"] = new_price
            print("Đã cập nhật giá thành công")
            break
    else:
        print("Không tìm thấy sản phẩm")

def main():
    while True:
        choice = input("""
=====================================
    QUẢN LÝ CỬA HÀNG - MINI 
=====================================
1. Xem danh sách sản phẩm hiện có
2. Thêm 1 sản phẩm mới
3. Cập nhật giá sản phẩm theo ID
4. Thoát chương trình
=====================================
Lựa chọn của bạn (1-4): """)
    
        match choice:
            case "1":
                display_products()
            case "2":
                add_product()
            case "3":
                update_price()
            case "4":
                print("Thoát chương trình")
                break
            case _:
                print("Lỗi! Vui lòng nhập lại")  

main()