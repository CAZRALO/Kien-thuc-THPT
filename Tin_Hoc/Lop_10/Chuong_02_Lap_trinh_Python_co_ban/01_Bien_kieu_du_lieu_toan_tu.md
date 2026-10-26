# 📌 Chủ Đề: Biến, Kiểu Dữ Liệu và Toán Tử Trong Python

> **Chương trình:** Tin Học 10 (GDPT 2018 - Định hướng KHMT)  
> **Chương II:** Lập trình cơ bản với Python  
> **Ngôn ngữ:** Python 3.10+

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm biến, cách đặt tên biến đúng chuẩn PEP 8.
- Nắm rõ 4 kiểu dữ liệu cơ bản: số nguyên (`int`), số thực (`float`), chuỗi (`str`), logic (`bool`).
- Vận dụng thành thạo các toán tử số học (`+`, `-`, `*`, `/`, `//`, `%`, `**`), toán tử quan hệ và logic (`and`, `or`, `not`).
- Biết cách nhập xuất dữ liệu chuẩn bằng hàm `input()` và `print()`.

---

## 📖 I. Lý Thuyết Cốt Lõi

### 1. Biến trong Python
- Biến là tên gọi của một vùng nhớ lưu trữ giá trị.
- Python sử dụng cơ chế định kiểu động (Dynamic Typing), không cần khai báo kiểu dữ liệu trước:
```python
x = 10          # int
pi = 3.14159    # float
name = "Antigravity"  # str
is_active = True      # bool
```

### 2. Quy tắc đặt tên biến chuẩn PEP 8
- Tên biến chỉ chứa chữ cái tiếng Anh (`a-z`, `A-Z`), chữ số (`0-9`) và dấu gạch dưới (`_`).
- **Không** được bắt đầu bằng chữ số (ví dụ: `2x` là lỗi).
- **Phân biệt** chữ hoa và chữ thường (`age` khác `Age`).
- Tránh trùng với các từ khoá (keywords): `def`, `class`, `if`, `for`, `while`, `import`...

---

## 🔢 II. Hệ Thống Toán Tử Python

| Loại Toán Tử | Kí Hiệu | Tên Gọi | Ví Dụ | Kết Quả |
|:---|:---:|:---|:---|:---:|
| **Số học** | `+` | Phép cộng | `7 + 3` | `10` |
| | `-` | Phép trừ | `7 - 3` | `4` |
| | `*` | Phép nhân | `7 * 3` | `21` |
| | `/` | Chia thực (trả về float) | `7 / 2` | `3.5` |
| | `//` | Chia lấy phần nguyên (Floor div) | `7 // 2` | `3` |
| | `%` | Chia lấy dư (Modulo) | `7 % 3` | `1` |
| | `**` | Luỹ thừa | `2 ** 4` | `16` |
| **So sánh** | `==`, `!=` | Bằng, khác | `5 == 5` | `True` |
| | `>`, `<`, `>=`, `<=` | So sánh lớn bé | `10 >= 8` | `True` |
| **Logic** | `and` | Và (đúng khi cả hai cùng đúng) | `(5 > 3) and (2 > 4)` | `False` |
| | `or` | Hoặc (đúng khi ít nhất một vế đúng) | `(5 > 3) or (2 > 4)` | `True` |
| | `not` | Phủ định logic | `not (5 > 3)` | `False` |

---

## 💻 III. Ví Dụ Code Mẫu & Phương Pháp Giải

### Bài toán: Tính chỉ số khối cơ thể (BMI) và phân loại
Chỉ số BMI được tính theo công thức:
$$\text{BMI} = \frac{m}{h^2}$$
*(với $m$ là cân nặng tính bằng kg, $h$ là chiều cao tính bằng mét)*.

```python
# Chương trình tính và đánh giá chỉ số BMI
def tinh_bmi(can_nang_kg: float, chieu_cao_m: float) -> tuple[float, str]:
    bmi = can_nang_kg / (chieu_cao_m ** 2)
    
    if bmi < 18.5:
        danh_gia = "Thiếu cân (Gầy)"
    elif bmi < 24.9:
        danh_gia = "Bình thường (Lý tưởng)"
    elif bmi < 29.9:
        danh_gia = "Thừa cân"
    else:
        danh_gia = "Béo phì"
        
    return bmi, danh_gia

# Chạy thử nghiệm
if __name__ == "__main__":
    m = float(input("Nhập cân nặng (kg): "))
    h = float(input("Nhập chiều cao (m): "))
    
    chi_so, phan_loai = tinh_bmi(m, h)
    print(f"-> Chỉ số BMI của bạn: {chi_so:.2f}")
    print(f"-> Đánh giá: {phan_loai}")
```
