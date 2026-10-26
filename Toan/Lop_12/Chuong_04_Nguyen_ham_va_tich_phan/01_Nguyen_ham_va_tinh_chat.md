# 📌 Chủ Đề: Nguyên Hàm và Các Tính Chất Cơ Bản

> **Chương trình:** Toán 12 (GDPT 2018)  
> **Chương IV:** Nguyên hàm và Tích phân  
> **Mức độ:** Nhận biết - Thông hiểu - Vận dụng

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa nguyên hàm của một hàm số trên một khoảng $K$.
- Nắm vững định lý về họ nguyên hàm $F(x) + C$.
- Ghi nhớ và sử dụng bảng nguyên hàm của các hàm số sơ cấp cơ bản và hàm số hợp $u = ax + b$.
- Áp dụng các tính chất tuyến tính của nguyên hàm để phân tích và tính toán.

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Định nghĩa Nguyên Hàm
Cho hàm số $f(x)$ xác định trên khoảng $K$.
Hàm số $F(x)$ được gọi là **nguyên hàm** của $f(x)$ trên $K$ nếu:
$$F'(x) = f(x), \quad \forall x \in K$$

### 2. Định lý về họ nguyên hàm
Nếu $F(x)$ là một nguyên hàm của $f(x)$ trên $K$ thì:
- Mọi nguyên hàm của $f(x)$ trên $K$ đều có dạng:
  $$\int f(x) \, dx = F(x) + C \quad (C \in \mathbb{R})$$

### 3. Các tính chất cơ bản
1. $\left(\int f(x) \, dx\right)' = f(x)$ và $\int f'(x) \, dx = f(x) + C$.
2. $\int k \cdot f(x) \, dx = k \int f(x) \, dx$ *(với hằng số $k \ne 0$)*.
3. $\int [f(x) \pm g(x)] \, dx = \int f(x) \, dx \pm \int g(x) \, dx$.

---

## 🔢 II. Bảng Nguyên Hàm Sơ Cấp & Mở Rộng

| Hàm Cơ Bản $\int f(x) \, dx$ | Nguyên Hàm Mở Rộng $\int f(ax + b) \, dx$ $(a \ne 0)$ |
|:---|:---|
| $\int 0 \, dx = C$ | |
| $\int dx = x + C$ | $\int dx = x + C$ |
| $\int x^\alpha \, dx = \frac{x^{\alpha + 1}}{\alpha + 1} + C$ $(\alpha \ne -1)$ | $\int (ax + b)^\alpha \, dx = \frac{1}{a} \cdot \frac{(ax + b)^{\alpha + 1}}{\alpha + 1} + C$ |
| $\int \frac{1}{x} \, dx = \ln|x| + C$ | $\int \frac{1}{ax + b} \, dx = \frac{1}{a} \ln|ax + b| + C$ |
| $\int e^x \, dx = e^x + C$ | $\int e^{ax + b} \, dx = \frac{1}{a} e^{ax + b} + C$ |
| $\int a^x \, dx = \frac{a^x}{\ln a} + C$ $(0 < a \ne 1)$ | $\int a^{mx + n} \, dx = \frac{1}{m} \cdot \frac{a^{mx + n}}{\ln a} + C$ |
| $\int \cos x \, dx = \sin x + C$ | $\int \cos(ax + b) \, dx = \frac{1}{a} \sin(ax + b) + C$ |
| $\int \sin x \, dx = -\cos x + C$ | $\int \sin(ax + b) \, dx = -\frac{1}{a} \cos(ax + b) + C$ |
| $\int \frac{1}{\cos^2 x} \, dx = \tan x + C$ | $\int \frac{1}{\cos^2(ax + b)} \, dx = \frac{1}{a} \tan(ax + b) + C$ |
| $\int \frac{1}{\sin^2 x} \, dx = -\cot x + C$ | $\int \frac{1}{\sin^2(ax + b)} \, dx = -\frac{1}{a} \cot(ax + b) + C$ |

---

## 📊 III. Sơ Đồ Phương Pháp Tìm Nguyên Hàm

```mermaid
graph TD
    Start[Tìm Nguyên Hàm I = ∫ f x dx] --> Check1{Có trong Bảng Nguyên hàm?}
    Check1 -- Có --> Formula[Áp dụng trực tiếp công thức]
    Check1 -- Không --> Check2{Có dạng u'(x) . g(u(x)) ?}
    Check2 -- Đúng --> Sub[Đổi biến số: Đặt t = u x]
    Check2 -- Sai --> Check3{Có tích hai hàm khác loại: đa thức, lượng giác, mũ, ln?}
    Check3 -- Đúng --> Parts[Nguyên hàm từng phần: ∫ u dv = u.v - ∫ v du]
    
    style Start fill:#e0f2fe,stroke:#0284c7,stroke-width:2px
    style Formula fill:#dcfce7,stroke:#16a34a,stroke-width:2px
    style Sub fill:#fef3c7,stroke:#d97706,stroke-width:2px
    style Parts fill:#f3e8ff,stroke:#9333ea,stroke-width:2px
```

---

## 📝 IV. Ví Dụ Minh Họa Có Lời Giải

**Ví dụ:** Tìm nguyên hàm $I = \int (3x^2 - 4\sin 2x + e^{3x}) \, dx$.

**Lời giải:**
Áp dụng tính chất tuyến tính của nguyên hàm:
$$I = 3\int x^2 \, dx - 4\int \sin 2x \, dx + \int e^{3x} \, dx$$
- Ta có:
  - $\int x^2 \, dx = \frac{x^3}{3}$
  - $\int \sin 2x \, dx = -\frac{1}{2}\cos 2x$
  - $\int e^{3x} \, dx = \frac{1}{3}e^{3x}$
- Thay vào biểu thức $I$:
  $$I = 3 \cdot \frac{x^3}{3} - 4 \left(-\frac{1}{2}\cos 2x\right) + \frac{1}{3}e^{3x} + C$$
  $$I = x^3 + 2\cos 2x + \frac{1}{3}e^{3x} + C$$
