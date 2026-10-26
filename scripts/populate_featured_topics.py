# -*- coding: utf-8 -*-
"""
Script soạn thảo nội dung mẫu chuẩn chuyên sâu với công thức LaTeX và hình biểu diễn SVG/Mermaid
"""

import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written {path}")

# ==============================================================================
# 1. TOÁN 12 - TÍNH ĐƠN ĐIỆU CỦA HÀM SỐ
# ==============================================================================
TOAN_12_DON_DIEU = """# 📌 Chủ Đề: Tính Đơn Điệu Của Hàm Số

> **Chương trình:** Toán 12 (GDPT 2018)  
> **Chương I:** Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số  
> **Mức độ:** Nhận biết - Thông hiểu - Vận dụng

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa hàm số đồng biến (tăng) và nghịch biến (giảm) trên một khoảng, đoạn hoặc nửa khoảng.
- Nắm vững mối liên hệ giữa dấu của đạo hàm cấp một $f'(x)$ và tính đơn điệu của hàm số $f(x)$.
- Thành thạo các bước lập bảng biến thiên và kết luận khoảng đơn điệu.
- Vận dụng giải các bài toán chứa tham số $m$ để hàm số đơn điệu trên từng khoảng xác định hoặc trên $\\mathbb{R}$.

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Định nghĩa tính đơn điệu
Kí hiệu $K$ là một khoảng, một đoạn hoặc một nửa khoảng. Giả sử hàm số $y = f(x)$ xác định trên $K$.
- Hàm số $y = f(x)$ gọi là **đồng biến (tăng)** trên $K$ nếu:
  $$\\forall x_1, x_2 \\in K: x_1 < x_2 \\implies f(x_1) < f(x_2)$$
- Hàm số $y = f(x)$ gọi là **nghịch biến (giảm)** trên $K$ nếu:
  $$\\forall x_1, x_2 \\in K: x_1 < x_2 \\implies f(x_1) > f(x_2)$$

### 2. Định lý về dấu của đạo hàm
Giả sử hàm số $y = f(x)$ có đạo hàm trên khoảng $K$:
1. Nếu $f'(x) > 0, \\forall x \\in K$ thì hàm số $f(x)$ **đồng biến** trên $K$.
2. Nếu $f'(x) < 0, \\forall x \\in K$ thì hàm số $f(x)$ **nghịch biến** trên $K$.
3. Nếu $f'(x) = 0, \\forall x \\in K$ thì hàm số $f(x)$ là **hàm hằng** trên $K$.

> **Định lý mở rộng:**  
> Nếu $f'(x) \\ge 0$ (hoặc $f'(x) \\le 0$), $\\forall x \\in K$ và dấu đẳng thức $f'(x) = 0$ chỉ xảy ra tại một số hữu hạn điểm trên $K$ thì hàm số $f(x)$ **đồng biến** (hoặc **nghịch biến**) trên $K$.

---

## 🔢 II. Hệ Thống Công Thức Cần Nhớ

| Hàm Số | Đạo Hàm $y'$ | Điều Kiện Đồng Biến Trên $\\mathbb{R}$ | Điều Kiện Nghịch Biến Trên $\\mathbb{R}$ |
|:---|:---|:---|:---|
| **Bậc ba:** $y = ax^3 + bx^2 + cx + d$ $(a \\ne 0)$ | $y' = 3ax^2 + 2bx + c$ | $\\begin{cases} a > 0 \\\\ \\Delta' \\le 0 \\end{cases}$ | $\\begin{cases} a < 0 \\\\ \\Delta' \\le 0 \\end{cases}$ |
| **Phân thức bậc nhất:** $y = \\frac{ax + b}{cx + d}$ $(ad - bc \\ne 0)$ | $y' = \\frac{ad - bc}{(cx + d)^2}$ | $ad - bc > 0$ trên từng khoảng $XĐ$ | $ad - bc < 0$ trên từng khoảng $XĐ$ |
| **Phân thức bậc hai / bậc nhất:** $y = \\frac{ax^2 + bx + c}{mx + n}$ | $y' = \\frac{amx^2 + 2anx + (bn - cm)}{(mx + n)^2}$ | $y' \\ge 0$ trên tập xác định | $y' \\le 0$ trên tập xác định |

---

## 📊 III. Sơ Đồ Tư Duy & Hình Biểu Diễn Trực Quan

### 1. Sơ đồ tư duy các bước xét tính đơn điệu (Mermaid)

```mermaid
graph TD
    A[Bước 1: Tìm tập xác định D của hàm số] --> B[Bước 2: Tính đạo hàm y' = f' x]
    B --> C[Bước 3: Tìm nghiệm x_i của y' = 0 hoặc điểm y' không xác định]
    C --> D[Bước 4: Sắp xếp các nghiệm và lập Bảng Biến Thiên]
    D --> E[Bước 5: Xét dấu y' và Kết luận các khoảng đồng biến / nghịch biến]
    
    style A fill:#e0f2fe,stroke:#0284c7,stroke-width:2px
    style B fill:#fef3c7,stroke:#d97706,stroke-width:2px
    style C fill:#dcfce7,stroke:#16a34a,stroke-width:2px
    style D fill:#f3e8ff,stroke:#9333ea,stroke-width:2px
    style E fill:#ffe4e6,stroke:#e11d48,stroke-width:2px
```

### 2. Hình biểu diễn: Minh họa đồ thị và tiếp tuyến có hệ số góc $k = f'(x)$ (SVG)

<div align="center">
<svg width="600" height="280" viewBox="0 0 600 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>

  <!-- Background Card -->
  <rect width="600" height="280" rx="12" fill="#0f172a" stroke="#1e293b" stroke-width="2"/>

  <!-- Left: Đồng biến -->
  <g transform="translate(30, 20)">
    <text x="110" y="25" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Đồng Biến: f'(x) &gt; 0</text>
    <!-- Axes -->
    <line x1="20" y1="200" x2="220" y2="200" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"/>
    <line x1="40" y1="210" x2="40" y2="40" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"/>
    <text x="220" y="215" fill="#94a3b8" font-size="12">x</text>
    <text x="30" y="45" fill="#94a3b8" font-size="12">y</text>
    <!-- Curve -->
    <path d="M 45 180 C 100 170, 140 100, 200 60" fill="none" stroke="#22c55e" stroke-width="3"/>
    <!-- Tangent line -->
    <line x1="80" y1="180" x2="180" y2="70" stroke="#f59e0b" stroke-dasharray="4" stroke-width="2"/>
    <circle cx="130" cy="125" r="4" fill="#f59e0b"/>
    <text x="140" y="125" fill="#f59e0b" font-size="11">Tiếp tuyến dốc lên (k &gt; 0)</text>
    <text x="110" y="235" fill="#cbd5e1" font-size="12" text-anchor="middle">Đồ thị đi lên từ trái sang phải</text>
  </g>

  <!-- Vertical separator -->
  <line x1="295" y1="30" x2="295" y2="250" stroke="#334155" stroke-dasharray="4"/>

  <!-- Right: Nghịch biến -->
  <g transform="translate(320, 20)">
    <text x="110" y="25" fill="#f43f5e" font-size="14" font-weight="bold" text-anchor="middle">Nghịch Biến: f'(x) &lt; 0</text>
    <!-- Axes -->
    <line x1="20" y1="200" x2="220" y2="200" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"/>
    <line x1="40" y1="210" x2="40" y2="40" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow)"/>
    <text x="220" y="215" fill="#94a3b8" font-size="12">x</text>
    <text x="30" y="45" fill="#94a3b8" font-size="12">y</text>
    <!-- Curve -->
    <path d="M 45 60 C 100 100, 140 170, 200 180" fill="none" stroke="#ef4444" stroke-width="3"/>
    <!-- Tangent line -->
    <line x1="80" y1="70" x2="180" y2="180" stroke="#f59e0b" stroke-dasharray="4" stroke-width="2"/>
    <circle cx="130" cy="125" r="4" fill="#f59e0b"/>
    <text x="140" y="115" fill="#f59e0b" font-size="11">Tiếp tuyến dốc xuống (k &lt; 0)</text>
    <text x="110" y="235" fill="#cbd5e1" font-size="12" text-anchor="middle">Đồ thị đi xuống từ trái sang phải</text>
  </g>
</svg>
<br>
<em>Hình 1.1: Ý nghĩa hình học của đạo hàm đối với tính đơn điệu</em>
</div>

---

## 💡 IV. Các Dạng Bài Tập & Phương Pháp Giải

### Dạng 1: Xét tính đơn điệu của hàm số cho trước
- **Phương pháp giải:**
  1. Tìm tập xác định $D$.
  2. Tính đạo hàm $y' = f'(x)$.
  3. Giải phương trình $y' = 0$ tìm các nghiệm $x_i \\in D$ hoặc các điểm làm cho $y'$ không xác định.
  4. Lập bảng xét dấu $y'$ (Bảng biến thiên).
  5. Đọc kết luận các khoảng đồng biến (nơi $y' > 0$) và nghịch biến (nơi $y' < 0$).

### Dạng 2: Tìm tham số $m$ để hàm số đơn điệu trên khoảng $(a; b)$
- **Phương pháp 1 (Cô lập tham số $m$):**  
  Biến đổi điều kiện $y' \\ge 0 \\iff m \\ge g(x)$ (hoặc $m \\le g(x)$), $\\forall x \\in (a; b)$.  
  - $m \\ge g(x), \\forall x \\in (a; b) \\iff m \\ge \\max_{[a; b]} g(x)$ (nếu tồn tại $\\max$).  
  - $m \\le g(x), \\forall x \\in (a; b) \\iff m \\le \\min_{[a; b]} g(x)$ (nếu tồn tại $\\min$).
- **Phương pháp 2 (Dùng định lý tam thức bậc hai):**  
  Khi không cô lập được $m$, áp dụng dấu của tam thức bậc hai $g(x) = Ax^2 + Bx + C$ với $\\Delta$ và so sánh nghiệm với các đầu mút.

---

## 📝 V. Ví Dụ Minh Họa Có Lời Giải Chi Tiết

### Ví dụ 1 (Mức độ Nhận biết - Thông hiểu):
**Đề bài:** Xét sự biến thiên của hàm số $y = x^3 - 3x^2 + 2$.

**Lời giải chi tiết:**
1. **Tập xác định:** $D = \\mathbb{R}$.
2. **Đạo hàm:**
   $$y' = 3x^2 - 6x = 3x(x - 2)$$
   $$y' = 0 \\iff \\left[\\begin{array}{l} x = 0 \\\\ x = 2 \\end{array}\\right.$$
3. **Bảng biến thiên:**

| $x$ | $-\\infty$ | | $0$ | | $2$ | | $+\\infty$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $y'$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
| $y$ | $-\\infty$ | $\\nearrow$ | $2$ | $\\searrow$ | $-2$ | $\\nearrow$ | $+\\infty$ |

4. **Kết luận:**
   - Hàm số đồng biến trên các khoảng $(-\\infty; 0)$ và $(2; +\\infty)$.
   - Hàm số nghịch biến trên khoảng $(0; 2)$.

---

### Ví dụ 2 (Mức độ Vận dụng):
**Đề bài:** Tìm tất cả các giá trị của tham số $m$ để hàm số $y = \\frac{1}{3}x^3 - mx^2 + (m^2 - 4)x + 3$ đồng biến trên $\\mathbb{R}$.

**Lời giải chi tiết:**
1. Tập xác định: $D = \\mathbb{R}$.
2. Đạo hàm:
   $$y' = x^2 - 2mx + (m^2 - 4)$$
   Hàm số đã cho đồng biến trên $\\mathbb{R}$ khi và chỉ khi:
   $$y' \\ge 0, \\forall x \\in \\mathbb{R} \\iff x^2 - 2mx + (m^2 - 4) \\ge 0, \\forall x \\in \\mathbb{R}$$
3. Vì tam thức bậc hai có hệ số $a = 1 > 0$, nên điều kiện tương đương:
   $$\\Delta' \\le 0 \\iff (-m)^2 - 1.(m^2 - 4) \\le 0$$
   $$\\iff m^2 - m^2 + 4 \\le 0 \\iff 4 \\le 0 \\text{ (Vô lí!)}$$
4. **Kết luận:** Không tồn tại giá trị nào của tham số $m$ thỏa mãn yêu cầu bài toán.

---

## ⚡ VI. Tóm Tắt Ghi Nhớ Nhanh (Cheat Sheet)

> [!TIP]
> - Nếu hàm số đồng biến trên $(a; b)$ và liên tục tại các đầu mút $a, b$ thì ta được phép kết luận hàm số đồng biến trên đoạn $[a; b]$.
> - Đối với hàm phân thức hữu tỉ bậc nhất $y = \\frac{ax + b}{cx + d}$, dấu của đạo hàm **không có dấu bằng**:  
>   $$y' = \\frac{ad - bc}{(cx + d)^2} > 0 \\implies ad - bc > 0$$ (không được lấy dấu bằng vì khi $ad - bc = 0$ hàm trở thành hàm hằng).
"""

# ==============================================================================
# 2. VẬT LÍ 11 - DAO ĐỘNG ĐIỀU HOÀ
# ==============================================================================
VAT_LY_11_DAO_DONG = """# 📌 Chủ Đề: Dao Động Điều Hoà

> **Chương trình:** Vật Lí 11 (GDPT 2018)  
> **Chương I:** Dao động cơ học  
> **Mức độ:** Nhận biết - Thông hiểu - Vận dụng cao

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững định nghĩa dao động, dao động tuần hoàn và dao động điều hoà.
- Thuộc và hiểu ý nghĩa các đại lượng trong phương trình dao động điều hoà: li độ $x$, biên độ $A$, pha dao động $(\\omega t + \\varphi)$, tần số góc $\\omega$, chu kì $T$, tần số $f$.
- Viết được phương trình vận tốc $v$, gia tốc $a$ và phân tích mối quan hệ lệch pha giữa $x$, $v$, $a$.
- Sử dụng thành thạo mối liên hệ giữa dao động điều hoà và chuyển động tròn đều qua vòng tròn lượng giác (VTLG).

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Khái niệm cơ bản
- **Dao động cơ:** Là chuyển động qua lại quanh một vị trí cân bằng (VTCB).
- **Dao động tuần hoàn:** Là dao động mà sau những khoảng thời gian bằng nhau gọi là chu kì, trạng thái dao động (vị trí, chiều và độ lớn vận tốc) của vật được lặp lại như cũ.
- **Dao động điều hoà:** Là dao động trong đó li độ của vật là một hàm côsin (hoặc sin) của thời gian.

### 2. Phương trình li độ
$$x = A \\cos(\\omega t + \\varphi)$$
Trong đó:
- $x$: Li độ dao động (đơn vị: $cm$ hoặc $m$), khoảng cách đại số từ vật đến VTCB. $(-A \\le x \\le A)$
- $A$: Biên độ dao động ($A > 0$), là độ lệch cực đại của vật so với VTCB.
- $\\omega$: Tần số góc (đơn vị: $rad/s$), $\\omega > 0$.
- $(\\omega t + \\varphi)$: Pha của dao động tại thời điểm $t$ (đơn vị: $rad$), xác định trạng thái dao động.
- $\\varphi$: Pha ban đầu tại thời điểm $t = 0$ (đơn vị: $rad$), thường quy ước $-\\pi \\le \\varphi \\le \\pi$.

---

## 🔢 II. Hệ Thống Công Thức Cốt Lõi

### 1. Mối liên hệ chu kì, tần số và tần số góc
$$T = \\frac{2\\pi}{\\omega} = \\frac{1}{f} = \\frac{\\Delta t}{N} \\quad \\Longleftrightarrow \\quad \\omega = \\frac{2\\pi}{T} = 2\\pi f$$
*(với $N$ là số dao động toàn phần thực hiện được trong thời gian $\\Delta t$)*.

### 2. Bộ 3 phương trình chuyển động: Li độ - Vận tốc - Gia tốc

| Đại Lượng | Biểu Thức Tức Thời | Giá Trị Cực Đại (Max) | Giá Trị Cực Tiểu (Min) | Độ Lệch Pha So Với $x$ |
|:---|:---|:---|:---|:---|
| **Li độ** $x$ | $x = A\\cos(\\omega t + \\varphi)$ | $x_{\\max} = +A$ (Biên dương) | $x_{\\min} = -A$ (Biên âm) | $0$ (Gốc chuẩn) |
| **Vận tốc** $v$ | $v = x' = -\\omega A\\sin(\\omega t + \\varphi) = \\omega A\\cos\\left(\\omega t + \\varphi + \\frac{\\pi}{2}\\right)$ | $v_{\\max} = \\omega A$ (Qua VTCB theo chiều dương) | $v_{\\min} = -\\omega A$ (Qua VTCB theo chiều âm) | Sớm pha $\\frac{\\pi}{2}$ (Vuông pha) |
| **Gia tốc** $a$ | $a = v' = -\\omega^2 A\\cos(\\omega t + \\varphi) = -\\omega^2 x = \\omega^2 A\\cos(\\omega t + \\varphi + \\pi)$ | $a_{\\max} = \\omega^2 A$ (Tại biên âm $x = -A$) | $a_{\\min} = -\\omega^2 A$ (Tại biên dương $x = +A$) | Sớm pha $\\pi$ (Ngược pha) |

### 3. Hệ thức độc lập thời gian (Công thức vuông pha)
Do $x$ và $v$ vuông pha:
$$\\left(\\frac{x}{A}\\right)^2 + \\left(\\frac{v}{\\omega A}\\right)^2 = 1 \\implies A^2 = x^2 + \\frac{v^2}{\\omega^2} \\implies v = \\pm \\omega \\sqrt{A^2 - x^2}$$

Do $v$ và $a$ vuông pha:
$$\\left(\\frac{v}{v_{\\max}}\\right)^2 + \\left(\\frac{a}{a_{\\max}}\\right)^2 = 1 \\implies \\left(\\frac{v}{\\omega A}\\right)^2 + \\left(\\frac{a}{\\omega^2 A}\\right)^2 = 1 \\implies A^2 = \\frac{v^2}{\\omega^2} + \\frac{a^2}{\\omega^4}$$

---

## 📊 III. Hình Biểu Diễn & Vòng Tròn Lượng Giác

### 1. Vòng tròn lượng giác biểu diễn pha dao động (SVG)

<div align="center">
<svg width="480" height="360" viewBox="0 0 480 360" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-v" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
    </marker>
  </defs>

  <!-- Background -->
  <rect width="480" height="360" rx="12" fill="#0f172a" stroke="#334155" stroke-width="2"/>

  <!-- Center (240, 180) Radius = 120 -->
  <!-- Main circle -->
  <circle cx="240" cy="180" r="120" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="2 4"/>

  <!-- Axes -->
  <line x1="60" y1="180" x2="420" y2="180" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-v)"/>
  <text x="425" y="185" fill="#38bdf8" font-size="14" font-weight="bold">x</text>

  <line x1="240" y1="330" x2="240" y2="30" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow-v)"/>
  <text x="245" y="30" fill="#94a3b8" font-size="14">y</text>

  <!-- Labels on Axis -->
  <text x="230" y="198" fill="#e2e8f0" font-size="14">O</text>
  <text x="360" y="200" fill="#22c55e" font-size="14" font-weight="bold">+A</text>
  <text x="100" y="200" fill="#ef4444" font-size="14" font-weight="bold">-A</text>

  <!-- Rotating Vector M -->
  <!-- Angle 45 deg: x = 240 + 120*cos(-45) = 240 + 84.85 = 325, y = 180 - 84.85 = 95 -->
  <line x1="240" y1="180" x2="325" y2="95" stroke="#f59e0b" stroke-width="3"/>
  <circle cx="325" cy="95" r="6" fill="#f59e0b"/>
  <text x="335" y="90" fill="#f59e0b" font-weight="bold" font-size="13">M(t)</text>

  <!-- Projection P -->
  <line x1="325" y1="95" x2="325" y2="180" stroke="#f59e0b" stroke-dasharray="4" stroke-width="1.5"/>
  <circle cx="325" cy="180" r="5" fill="#38bdf8"/>
  <text x="320" y="205" fill="#38bdf8" font-weight="bold" font-size="13">x = A.cos(Φ)</text>

  <!-- Angle arc -->
  <path d="M 280 180 A 40 40 0 0 0 268 152" fill="none" stroke="#f59e0b" stroke-width="2"/>
  <text x="282" y="165" fill="#f59e0b" font-size="12">Φ = ωt + φ</text>

  <!-- Direction of Rotation -->
  <path d="M 210 70 A 130 130 0 0 1 270 70" fill="none" stroke="#ec4899" stroke-width="2" marker-end="url(#arrow-v)"/>
  <text x="240" y="55" fill="#ec4899" font-size="12" text-anchor="middle">Chiều quay ngược chiều kim đồng hồ (ω &gt; 0)</text>

  <!-- Half planes -->
  <text x="240" y="320" fill="#10b981" font-size="12" text-anchor="middle">Nửa dưới vòng tròn: Vật chuyển động theo CHIỀU DƯƠNG (v &gt; 0)</text>
  <text x="240" y="140" fill="#f43f5e" font-size="12" text-anchor="middle">Nửa trên: Vật chuyển động theo CHIỀU ÂM (v &lt; 0)</text>
</svg>
<br>
<em>Hình 1.2: Kĩ thuật vòng tròn lượng giác xác định trạng thái và thời gian dao động</em>
</div>

---

## 💡 IV. Các Dạng Bài Tập & Phương Pháp Giải

### Dạng 1: Xác định các đại lượng đặc trưng từ phương trình dao động
- Đưa phương trình về dạng chuẩn $x = A\\cos(\\omega t + \\varphi)$ với $A > 0$.
- Áp dụng các quy tắc biến đổi góc phụ và góc đối:
  - $-\\cos(\\alpha) = \\cos(\\alpha \\pm \\pi)$
  - $\\sin(\\alpha) = \\cos\\left(\\alpha - \\frac{\\pi}{2}\\right)$
  - $-\\sin(\\alpha) = \\cos\\left(\\alpha + \\frac{\\pi}{2}\\right)$

### Dạng 2: Ứng dụng vòng tròn lượng giác tìm thời gian ngắn nhất $\\Delta t$
1. Xác định vị trí ban đầu $x_1$ và vị trí sau $x_2$ trên vòng tròn tương ứng với góc pha $\\Phi_1, \\Phi_2$.
2. Góc quét của vectơ quay: $\\Delta \\alpha = |\\Phi_2 - \\Phi_1|$ (tính bằng radian).
3. Thời gian quét:
   $$\\Delta t = \\frac{\\Delta \\alpha}{\\omega} = \\frac{\\Delta \\alpha}{2\\pi} \\cdot T$$

---

## 📝 V. Ví Dụ Minh Họa Có Lời Giải Chi Tiết

### Ví dụ 1:
**Đề bài:** Một vật dao động điều hoà có phương trình: $x = 4\\cos\\left(5\\pi t - \\frac{\\pi}{3}\\right)$ ($cm$).
1. Tìm biên độ, chu kì, tần số và tần số góc của dao động.
2. Viết phương trình vận tốc và gia tốc của vật.
3. Tính vận tốc và gia tốc của vật khi vật đi qua vị trí có li độ $x = 2\\sqrt{3}$ $cm$ theo chiều âm.

**Lời giải chi tiết:**
1. **Các đại lượng đặc trưng:**
   - Biên độ: $A = 4\\text{ cm}$.
   - Tần số góc: $\\omega = 5\\pi\\text{ rad/s}$.
   - Chu kì: $T = \\frac{2\\pi}{\\omega} = \\frac{2\\pi}{5\\pi} = 0,4\\text{ s}$.
   - Tần số: $f = \\frac{1}{T} = 2,5\\text{ Hz}$.

2. **Phương trình vận tốc và gia tốc:**
   - Phương trình vận tốc:
     $$v = x' = -20\\pi \\sin\\left(5\\pi t - \\frac{\\pi}{3}\\right) = 20\\pi \\cos\\left(5\\pi t + \\frac{\\pi}{6}\\right)\\text{ (cm/s)}$$
   - Phương trình gia tốc:
     $$a = -\\omega^2 x = -100\\pi^2 \\cos\\left(5\\pi t - \\frac{\\pi}{3}\\right)\\text{ (cm/s}^2\\text{)}$$

3. **Tính $v$ và $a$ tại $x = 2\\sqrt{3}$ cm theo chiều âm ($v < 0$):**
   - Áp dụng hệ thức độc lập:
     $$v = -\\omega \\sqrt{A^2 - x^2} = -5\\pi \\sqrt{4^2 - (2\\sqrt{3})^2} = -5\\pi \\sqrt{16 - 12} = -10\\pi\\text{ cm/s}$$
   - Gia tốc tại thời điểm đó:
     $$a = -\\omega^2 x = -(5\\pi)^2 \\cdot 2\\sqrt{3} = -50\\sqrt{3}\\pi^2\\text{ cm/s}^2 \\approx -500\\sqrt{3}\\text{ cm/s}^2 \\text{ (lấy } \\pi^2 \\approx 10\\text{)}$$

---

## ⚡ VI. Bảng Ghi Nhớ Nhanh Các Khoảng Thời Gian Vàng

| Quãng Đường Chuyển Động | Góc Quét $\\Delta \\alpha$ | Thời Gian Tối Thiểu $\\Delta t$ |
|:---|:---:|:---:|
| Từ $0 \\to \\frac{A}{2}$ hoặc $-\\frac{A}{2} \\to 0$ | $\\frac{\\pi}{6}$ | $\\frac{T}{12}$ |
| Từ $\\frac{A}{2} \\to \\frac{A\\sqrt{2}}{2}$ | $\\frac{\\pi}{12}$ | $\\frac{T}{24}$ |
| Từ $\\frac{A\\sqrt{2}}{2} \\to \\frac{A\\sqrt{3}}{2}$ | $\\frac{\\pi}{12}$ | $\\frac{T}{24}$ |
| Từ $\\frac{A\\sqrt{3}}{2} \\to A$ | $\\frac{\\pi}{6}$ | $\\frac{T}{12}$ |
| Từ $0 \\to A$ | $\\frac{\\pi}{2}$ | $\\frac{T}{4}$ |
| Từ $-A \\to +A$ | $\\pi$ | $\\frac{T}{2}$ |
"""

# ==============================================================================
# 3. HOÁ HỌC 12 - ESTER & LIPID
# ==============================================================================
HOA_HOC_12_ESTER = """# 📌 Chủ Đề: Ester - Cấu Tạo, Tính Chất & Điều Chế

> **Chương trình:** Hóa Học 12 (GDPT 2018)  
> **Chương I:** Ester - Lipid - Xà phòng và chất giặt rửa  
> **Mức độ:** Nhận biết - Thông hiểu - Vận dụng

---

## 🎯 Mục Tiêu Bài Học
- Nêu được khái niệm, công thức chung, đặc điểm cấu tạo phân tử của ester.
- Viết được công thức cấu tạo và gọi tên các ester theo danh pháp IUPAC và tên thông thường.
- Giải thích được tính chất vật lí (nhiệt độ sôi, tính tan, mùi hương đặc trưng).
- Trình bày được tính chất hoá học đặc trưng: Phản ứng thuỷ phân trong môi trường acid (thuận nghịch) và môi trường kiềm (xà phòng hoá một chiều).
- Thực hiện phương pháp điều chế ester bằng phản ứng ester hoá Fischer.

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Khái niệm và Cấu Tạo Phân Tử
Khi thay thế nhóm $-\\text{OH}$ ở nhóm carboxyl của carboxylic acid bằng nhóm $-\\text{OR}'$ thì thu được ester.

Công thức tổng quát của ester đơn chức:
$$R-\\text{COO}-R'$$
*(Trong đó $R$ là gốc hydrocarbon hoặc nguyên tử $H$; $R'$ là gốc hydrocarbon, $R' \\ne H$)*.

Ester no, đơn chức, mạch hở có công thức phân tử chung là:
$$\\text{C}_n\\text{H}_{2n}\\text{O}_2 \\quad (n \\ge 2)$$

### 2. Danh Pháp (Tên Gọi)
$$\\text{Tên ester} = \\text{Tên gốc hydrocarbon } R' + \\text{Tên gốc acid } R\\text{COO} (\\text{đuôi } \\textbf{-ate})$$

**Ví dụ:**
- $\\text{HCOOCH}_3$: Methyl formate
- $\\text{CH}_3\\text{COOC}_2\\text{H}_5$: Ethyl acetate
- $\\text{CH}_2=\\text{CH-COOCH}_3$: Methyl acrylate
- $\\text{CH}_3\\text{COOCH}_2\\text{C}_6\\text{H}_5$: Benzyl acetate (mùi hoa nhài)
- $\\text{CH}_3\\text{COOCH}_2\\text{CH}_2\\text{CH(CH}_3)_2$: Isoamyl acetate (mùi chuối chín)

---

## 🔢 II. Hệ Thống Tính Chất Hoá Học

### 1. Phản ứng thuỷ phân trong môi trường acid (Thuận nghịch)
$$R\\text{COO}R' + \\text{H}_2\\text{O} \\;\\xrightleftharpoons[\\text{t}^\\circ]{\\text{H}_2\\text{SO}_4\\text{ đặc}}\\; R\\text{COOH} + R'\\text{OH}$$

### 2. Phản ứng thuỷ phân trong môi trường kiềm (Phản ứng xà phòng hoá - Một chiều)
$$R\\text{COO}R' + \\text{NaOH} \\xrightarrow{\\text{t}^\\circ} R\\text{COONa} + R'\\text{OH}$$

### 3. Các trường hợp thuỷ phân đặc biệt

```mermaid
flowchart TD
    Ester[Ester R-COO-R'] --> Case1["1. R' có liên kết đôi đính trực tiếp vào -COO-<br/>R-COO-CH=CH-R''"]
    Ester --> Case2["2. R' là gốc Phenyl<br/>R-COO-C6H5"]
    Ester --> Case3["3. Ester của alcohol đa chức hoặc tạp chức"]

    Case1 -->|Thuỷ phân| Prod1["Tạo Aldehyde hoặc Ketone (không tạo alcohol bền)"]
    Case2 -->|+ 2 NaOH| Prod2["Tạo 2 Muối + H2O<br/>R-COONa + C6H5ONa + H2O"]
```

---

## 📊 III. Sơ Đồ Thiết Bị Thí Nghiệm Điều Chế Ester (SVG)

<div align="center">
<svg width="520" height="300" viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg">
  <!-- Card background -->
  <rect width="520" height="300" rx="12" fill="#0f172a" stroke="#334155" stroke-width="2"/>

  <!-- Title -->
  <text x="260" y="30" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">Thiết Bị Thí Nghiệm Điều Chế Ethyl Acetate (CH3COOC2H5)</text>

  <!-- Flask -->
  <path d="M 140 180 L 160 120 L 160 90 L 180 90 L 180 120 L 200 180 Z" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
  <ellipse cx="170" cy="180" rx="30" ry="10" fill="#3b82f6" opacity="0.6"/>
  <text x="170" y="165" fill="#e2e8f0" font-size="10" text-anchor="middle">CH3COOH + C2H5OH</text>
  <text x="170" y="177" fill="#fbbf24" font-size="10" text-anchor="middle">+ H2SO4 đặc + đá bọt</text>

  <!-- Heat burner -->
  <rect x="155" y="220" width="30" height="30" fill="#475569" rx="4"/>
  <polygon points="170,200 162,218 178,218" fill="#f97316"/>
  <text x="170" y="265" fill="#f97316" font-size="11" text-anchor="middle">Đèn cồn đun nhẹ (65-70°C)</text>

  <!-- Delivery Tube -->
  <path d="M 170 90 L 170 65 L 340 65 L 370 170" fill="none" stroke="#94a3b8" stroke-width="5" stroke-linecap="round"/>

  <!-- Cooling Beaker with ice water -->
  <rect x="330" y="150" width="80" height="90" fill="#0284c7" opacity="0.3" rx="6" stroke="#38bdf8" stroke-width="2"/>
  <text x="370" y="260" fill="#38bdf8" font-size="11" text-anchor="middle">Nước đá lạnh (ngưng tụ)</text>

  <!-- Collecting Test tube -->
  <rect x="355" y="140" width="30" height="85" fill="#334155" rx="6" stroke="#e2e8f0" stroke-width="1.5"/>
  <rect x="356" y="190" width="28" height="33" fill="#22c55e" opacity="0.7"/>
  <text x="370" y="210" fill="#ffffff" font-size="10" text-anchor="middle">Ester tách lớp</text>
  
  <!-- Callout note -->
  <rect x="25" y="80" width="100" height="50" rx="6" fill="#1e1e38" stroke="#818cf8"/>
  <text x="75" y="100" fill="#a5b4fc" font-size="10" text-anchor="middle">H2SO4 đặc:</text>
  <text x="75" y="115" fill="#e0e7ff" font-size="9" text-anchor="middle">- Xúc tác</text>
  <text x="75" y="125" fill="#e0e7ff" font-size="9" text-anchor="middle">- Hút nước (tăng H%)</text>
</svg>
<br>
<em>Hình 1.3: Mô hình phản ứng ester hoá và hệ thống ngưng tụ hơi ester</em>
</div>

---

## 💡 IV. Các Dạng Bài Tập & Phương Pháp Giải

### Dạng 1: Xác định công thức phân tử ester no đơn chức qua phản ứng đốt cháy
- Phương trình phản ứng:
  $$\\text{C}_n\\text{H}_{2n}\\text{O}_2 + \\frac{3n - 2}{2}\\text{O}_2 \\xrightarrow{\\text{t}^\\circ} n\\text{CO}_2 + n\\text{H}_2\\text{O}$$
- **Đặc điểm cốt lõi:**
  $$n_{\\text{CO}_2} = n_{\\text{H}_2\\text{O}}$$
  $$n_{\\text{ester}} = \\frac{n_{\\text{O(trong ester)}}}{2} = \\frac{2n_{\\text{CO}_2} + n_{\\text{H}_2\\text{O}} - 2n_{\\text{O}_2}}{2}$$
  $$n = \\frac{n_{\\text{CO}_2}}{n_{\\text{ester}}} \\implies M_{\\text{ester}} = 14n + 32$$

### Dạng 2: Bài toán phản ứng xà phòng hoá với dung dịch $\\text{NaOH}/\\text{KOH}$
- Áp dụng định luật bảo toàn khối lượng:
  $$m_{\\text{ester}} + m_{\\text{NaOH}} = m_{\\text{chất rắn (muối)}} + m_{\\text{alcohol}}$$
- Nếu $n_{\\text{NaOH phản ứng}} > n_{\\text{alcohol}}$, nghĩ ngay đến ester của phenol:
  $$R\\text{COO-C}_6\\text{H}_4-R' + 2\\text{NaOH} \\to R\\text{COONa} + R'-\\text{C}_6\\text{H}_4\\text{ONa} + \\text{H}_2\\text{O}$$

---

## 📝 V. Ví Dụ Minh Họa Có Lời Giải Chi Tiết

**Đề bài:** Đun nóng $8,8\\text{ g}$ ester no, đơn chức, mạch hở $X$ với $100\\text{ mL}$ dung dịch $\\text{NaOH } 1\\text{M}$ (vừa đủ). Sau phản ứng hoàn toàn, cô cạn dung dịch thu được $8,2\\text{ g}$ muối khan.
1. Xác định công thức phân tử và công thức cấu tạo của $X$.
2. Gọi tên ester $X$.

**Lời giải chi tiết:**
1. Số mol $\\text{NaOH}$:
   $$n_{\\text{NaOH}} = 0,1 \\times 1 = 0,1\\text{ mol}$$
   Vì $X$ là ester đơn chức nên:
   $$n_X = n_{\\text{muối}} = n_{\\text{NaOH}} = 0,1\\text{ mol}$$
2. Khối lượng mol phân tử của $X$:
   $$M_X = \\frac{m_X}{n_X} = \\frac{8,8}{0,1} = 88\\text{ (g/mol)}$$
   Vì $X$ no, đơn chức, mạch hở $\\implies \\text{C}_n\\text{H}_{2n}\\text{O}_2$:
   $$14n + 32 = 88 \\implies 14n = 56 \\implies n = 4$$
   Công thức phân tử là $\\text{C}_4\\text{H}_8\\text{O}_2$.
3. Khối lượng mol của muối $R\\text{COONa}$:
   $$M_{\\text{muối}} = \\frac{8,2}{0,1} = 82\\text{ (g/mol)}$$
   $$\\iff R + 67 = 82 \\implies R = 15\\text{ (gốc } -\\text{CH}_3)$$
4. Xác định gốc $R'$:
   $$R' = 88 - (15 + 44) = 29\\text{ (gốc } -\\text{C}_2\\text{H}_5)$$
5. **Kết luận:**
   - Công thức cấu tạo của $X$: $\\text{CH}_3\\text{COOC}_2\\text{H}_5$.
   - Tên gọi: **Ethyl acetate**.
"""

# ==============================================================================
# 4. TOÁN 10 - VECTƠ & CÁC PHÉP TOÁN
# ==============================================================================
TOAN_10_VECTO = """# 📌 Chủ Đề: Khái Niệm Vectơ và Các Phép Toán Vectơ

> **Chương trình:** Toán 10 (GDPT 2018)  
> **Chương IV:** Vectơ  
> **Mức độ:** Cơ bản - Nâng cao

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa vectơ, hướng, phương, độ dài của vectơ, hai vectơ cùng phương, cùng hướng, bằng nhau và đối nhau.
- Nắm vững và áp dụng quy tắc 3 điểm, quy tắc hình bình hành, quy tắc hiệu hai vectơ.
- Hiểu ý nghĩa hình học của trung điểm đoạn thẳng, trọng tâm tam giác dưới dạng hệ thức vectơ.

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Định nghĩa vectơ
Vectơ là một đoạn thẳng có hướng.
- Kí hiệu: $\\vec{a}, \\vec{b}$ hoặc $\\vec{AB}$ (điểm $A$ là điểm đầu, điểm $B$ là điểm cuối).
- Độ dài vectơ $\\vec{AB}$ là khoảng cách giữa $A$ và $B$, kí hiệu $|\\vec{AB}| = AB$.
- **Vectơ không** (kí hiệu $\\vec{0}$): Là vectơ có điểm đầu và điểm cuối trùng nhau (ví dụ $\\vec{AA}$). Độ dài bằng $0$, hướng tuỳ ý.

### 2. Hai vectơ cùng phương, cùng hướng
- Giá của vectơ: Đường thẳng đi qua điểm đầu và điểm cuối của vectơ đó.
- Hai vectơ gọi là **cùng phương** nếu giá của chúng song song hoặc trùng nhau.
- Nếu hai vectơ cùng phương thì chúng có thể **cùng hướng** hoặc **ngược hướng**.

---

## 🔢 II. Hệ Thống Các Quy Tắc Toán Học Vectơ

| Tên Quy Tắc | Biểu Thức Toán Học | Hình Minh Họa Ý Nghĩa |
|:---|:---|:---|
| **Quy tắc 3 điểm (Cộng nối tiếp)** | $\\vec{AB} + \\vec{BC} = \\vec{AC}$ | Điểm cuối của vectơ này là điểm đầu của vectơ kia |
| **Quy tắc hiệu** | $\\vec{AB} - \\vec{AC} = \\vec{CB}$ | Chung gốc $A$, lấy ngọn sau trừ ngọn trước |
| **Quy tắc hình bình hành** | $\\vec{AB} + \\vec{AD} = \\vec{AC}$ | Với $ABCD$ là hình bình hành ($AC$ là đường chéo) |
| **Tính chất trung điểm $I$ của $AB$** | $\\vec{IA} + \\vec{IB} = \\vec{0} \\iff \\vec{MA} + \\vec{MB} = 2\\vec{MI}$ | Đúng với mọi điểm $M$ bất kì |
| **Tính chất trọng tâm $G$ của $\\Delta ABC$** | $\\vec{GA} + \\vec{GB} + \\vec{GC} = \\vec{0} \\iff \\vec{MA} + \\vec{MB} + \\vec{MC} = 3\\vec{MG}$ | Đúng với mọi điểm $M$ bất kì |

---

## 📊 III. Hình Biểu Diễn Trực Quan (SVG)

<div align="center">
<svg width="560" height="260" viewBox="0 0 560 260" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-vec" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#38bdf8"/>
    </marker>
    <marker id="arrow-res" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#f43f5e"/>
    </marker>
  </defs>

  <rect width="560" height="260" rx="12" fill="#0f172a" stroke="#334155" stroke-width="2"/>

  <!-- Left: Quy tắc 3 điểm -->
  <g transform="translate(30, 20)">
    <text x="100" y="25" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">Quy Tắc 3 Điểm Tam Giác</text>
    
    <line x1="30" y1="180" x2="110" y2="90" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-vec)"/>
    <text x="15" y="195" fill="#f8fafc" font-size="13" font-weight="bold">A</text>
    <text x="55" y="125" fill="#38bdf8" font-size="12">AB</text>

    <line x1="110" y1="90" x2="200" y2="160" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-vec)"/>
    <text x="110" y="80" fill="#f8fafc" font-size="13" font-weight="bold">B</text>
    <text x="165" y="115" fill="#38bdf8" font-size="12">BC</text>

    <!-- Result AC -->
    <line x1="30" y1="180" x2="200" y2="160" stroke="#f43f5e" stroke-width="3" marker-end="url(#arrow-res)"/>
    <text x="210" y="170" fill="#f8fafc" font-size="13" font-weight="bold">C</text>
    <text x="115" y="200" fill="#f43f5e" font-size="13" font-weight="bold">AC = AB + BC</text>
  </g>

  <!-- Divider -->
  <line x1="260" y1="30" x2="260" y2="230" stroke="#334155" stroke-dasharray="4"/>

  <!-- Right: Quy tắc Hình bình hành -->
  <g transform="translate(290, 20)">
    <text x="120" y="25" fill="#22c55e" font-size="14" font-weight="bold" text-anchor="middle">Quy Tắc Hình Bình Hành</text>

    <!-- Side AB -->
    <line x1="40" y1="180" x2="160" y2="180" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-vec)"/>
    <text x="25" y="185" fill="#f8fafc" font-size="13" font-weight="bold">A</text>
    <text x="170" y="185" fill="#f8fafc" font-size="13" font-weight="bold">B</text>

    <!-- Side AD -->
    <line x1="40" y1="180" x2="90" y2="90" stroke="#38bdf8" stroke-width="2.5" marker-end="url(#arrow-vec)"/>
    <text x="85" y="80" fill="#f8fafc" font-size="13" font-weight="bold">D</text>

    <!-- Dashed sides -->
    <line x1="90" y1="90" x2="210" y2="90" stroke="#64748b" stroke-dasharray="3"/>
    <line x1="160" y1="180" x2="210" y2="90" stroke="#64748b" stroke-dasharray="3"/>
    <text x="220" y="90" fill="#f8fafc" font-size="13" font-weight="bold">C</text>

    <!-- Diagonal AC -->
    <line x1="40" y1="180" x2="210" y2="90" stroke="#f43f5e" stroke-width="3" marker-end="url(#arrow-res)"/>
    <text x="135" y="125" fill="#f43f5e" font-size="13" font-weight="bold">AC = AB + AD</text>
  </g>
</svg>
<br>
<em>Hình 1.4: Minh hoạ trực quan quy tắc cộng nối tiếp và quy tắc hình bình hành</em>
</div>

---

## 📝 IV. Ví Dụ Minh Họa Có Lời Giải

**Đề bài:** Cho tứ giác $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $CD$. Chứng minh rằng:
$$\\vec{AD} + \\vec{BC} = 2\\vec{MN}$$

**Lời giải chi tiết:**
- Theo quy tắc 3 điểm, ta chèn các điểm $M$ và $N$ vào hai vectơ ở vế trái:
  $$\\vec{AD} = \\vec{AM} + \\vec{MN} + \\vec{ND}$$
  $$\\vec{BC} = \\vec{BM} + \\vec{MN} + \\vec{NC}$$
- Cộng từng vế của hai đẳng thức trên, ta được:
  $$\\vec{AD} + \\vec{BC} = (\\vec{AM} + \\vec{BM}) + (\\vec{MN} + \\vec{MN}) + (\\vec{ND} + \\vec{NC})$$
- Vì $M$ là trung điểm của $AB$ nên $\\vec{AM} + \\vec{BM} = \\vec{0}$.
- Vì $N$ là trung điểm của $CD$ nên $\\vec{ND} + \\vec{NC} = \\vec{0}$.
- Do đó:
  $$\\vec{AD} + \\vec{BC} = \\vec{0} + 2\\vec{MN} + \\vec{0} = 2\\vec{MN} \\quad \\text{(Điều phải chứng minh)}$$
"""

# ==============================================================================
# 5. SINH HỌC 12 - GEN & TÁI BẢN ADN
# ==============================================================================
SINH_HOC_12_ADN = """# 📌 Chủ Đề: Gen, Mã Di Truyền và Quá Trình Tái Bản ADN

> **Chương trình:** Sinh Học 12 (GDPT 2018)  
> **Chương I:** Di truyền phân tử  
> **Mức độ:** Cơ bản đến Chuyên sâu

---

## 🎯 Mục Tiêu Bài Học
- Nêu được khái niệm gen, cấu trúc chung của một gen cấu trúc (Vùng điều hoà, Vùng mã hoá, Vùng kết thúc).
- Hiểu được các đặc điểm của mã di truyền: Mã bộ ba, tính phổ biến, tính đặc hiệu, tính thoái hoá.
- Trình bày diễn biến quá trình nhân đôi (tái bản) ADN theo nguyên tắc bổ sung và bán bảo tồn.
- Tính toán thành thạo các thông số phân tử: Số nucleotide, chiều dài, số liên kết hydrogen, số đoạn mồi RNA.

---

## 📖 I. Lý Thuyết Cốt Lõi

### 1. Cấu trúc của Gen
Gen là một đoạn phân tử ADN mang thông tin mã hoá cho một chuỗi polypeptide hay một phân tử ARN.

Cấu trúc một gen điển hình gồm 3 vùng theo chiều $3' \\to 5'$ trên mạch khuôn:
```mermaid
flowchart LR
    A["Vùng điều hoà (3')<br/>Chứa trình tự khởi động Promoter"] --> B["Vùng mã hoá<br/>Mang thông tin acid amin"]
    B --> C["Vùng kết thúc (5')<br/>Tín hiệu dừng phiên mã"]
```

### 2. Đặc điểm của Mã Di Truyền
Mã di truyền là mã bộ ba (triplet): Cứ 3 nucleotide liền kề trên mARN mã hoá cho 1 amino acid.
- **Có $4^3 = 64$ codon**, trong đó:
  - **1 codon mở đầu:** $5'\\text{AUG}3'$ (mã hoá Methionine ở sinh vật nhân thực, Formyl-methionine ở nhân sơ).
  - **3 codon kết thúc:** $5'\\text{UAA}3'$, $5'\\text{UAG}3'$, $5'\\text{UGA}3'$ (không mã hoá amino acid).
  - **61 codon** mã hoá cho 20 loại amino acid.
- **Đặc điểm cốt lõi:**
  1. *Tính liên tục:* Đọc từ một điểm xác định từng bộ ba một, không gối lên nhau.
  2. *Tính phổ biến:* Hầu hết mọi loài sinh vật đều dùng chung một bộ mã di truyền.
  3. *Tính đặc hiệu:* Mỗi codon chỉ mã hoá cho **duy nhất 1 loại** amino acid.
  4. *Tính thoái hoá (dư thừa):* Nhiều codon khác nhau cùng mã hoá cho **1 loại** amino acid (trừ AUG và UGG).

---

## 🔢 II. Quá Trình Tái Bản (Nhân Đôi) ADN

Quá trình nhân đôi ADN diễn ra ở pha S của kì trung gian trong chu kì tế bào, gồm 3 bước:
1. **Tháo xoắn phân tử ADN:** Nhờ enzyme DNA helicase và topoisomerase làm đứt các liên kết hydrogen, tạo chạc chữ Y.
2. **Tổng hợp mạch ADN mới:** 
   - Enzyme **RNA polymerase (primase)** tổng hợp đoạn mồi RNA ngắn có đầu $3'-\\text{OH}$ tự do.
   - Enzyme **DNA polymerase** di chuyển dọc trên mạch khuôn theo chiều $3' \\to 5'$ để kéo dài mạch mới theo chiều $5' \\to 3'$ tuân theo **nguyên tắc bổ sung** ($A - T$, $G - C$).
   - Mạch khuôn $3' \\to 5'$: Mạch mới được tổng hợp **liên tục**.
   - Mạch khuôn $5' \\to 3'$: Mạch mới tổng hợp **gián đoạn** thành từng đoạn ngắn **Okazaki**.
3. **Nối các đoạn Okazaki:** Enzyme cắt bỏ đoạn mồi, điền nucleotide ADN và enzyme **DNA ligase** nối liền mạch.

---

## 📊 III. Sơ Đồ Chạc Tái Bản ADN Chữ Y (SVG)

<div align="center">
<svg width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="600" height="300" rx="12" fill="#0f172a" stroke="#334155" stroke-width="2"/>

  <!-- Fork Title -->
  <text x="300" y="30" fill="#38bdf8" font-size="15" font-weight="bold" text-anchor="middle">Mô Hình Chạc Chữ Y Tái Bản ADN</text>

  <!-- Unwinding Fork -->
  <!-- Template Upper (3' to 5') -->
  <path d="M 50 80 L 300 80 L 550 50" fill="none" stroke="#60a5fa" stroke-width="4"/>
  <text x="40" y="85" fill="#60a5fa" font-weight="bold" font-size="13">3'</text>
  <text x="560" y="55" fill="#60a5fa" font-weight="bold" font-size="13">5'</text>

  <!-- Template Lower (5' to 3') -->
  <path d="M 50 220 L 300 220 L 550 250" fill="none" stroke="#60a5fa" stroke-width="4"/>
  <text x="40" y="225" fill="#60a5fa" font-weight="bold" font-size="13">5'</text>
  <text x="560" y="255" fill="#60a5fa" font-weight="bold" font-size="13">3'</text>

  <!-- Continuous new strand -->
  <path d="M 120 110 L 450 110" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4"/>
  <polygon points="450,110 440,105 440,115" fill="#22c55e"/>
  <text x="250" y="105" fill="#22c55e" font-size="11" font-weight="bold">Mạch dẫn đầu (Tổng hợp liên tục 5' -&gt; 3')</text>

  <!-- Discontinuous Okazaki fragments -->
  <!-- Fragment 1 -->
  <line x1="200" y1="190" x2="130" y2="190" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="130,190 140,185 140,195" fill="#f59e0b"/>
  <!-- Fragment 2 -->
  <line x1="330" y1="190" x2="240" y2="190" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="240,190 250,185 250,195" fill="#f59e0b"/>
  <!-- Fragment 3 -->
  <line x1="460" y1="190" x2="370" y2="190" stroke="#f59e0b" stroke-width="3"/>
  <polygon points="370,190 380,185 380,195" fill="#f59e0b"/>
  <text x="280" y="180" fill="#f59e0b" font-size="11" font-weight="bold">Các đoạn Okazaki (Tổng hợp gián đoạn)</text>

  <!-- Helicase enzyme icon -->
  <polygon points="530,150 490,120 490,180" fill="#ec4899" opacity="0.8"/>
  <text x="500" y="155" fill="#ffffff" font-size="10" text-anchor="middle">Helicase</text>
  <text x="500" y="195" fill="#ec4899" font-size="10" text-anchor="middle">Chiều tháo xoắn</text>
</svg>
<br>
<em>Hình 1.5: Chiều tổng hợp liên tục và gián đoạn tại chạc ba tái bản</em>
</div>

---

## 🔢 IV. Bảng Công Thức Tính Toán Phân Tử ADN

1. **Tổng số nucleotide của gen:**
   $$N = 2A + 2G = 2T + 2C$$
   $$A = T, \\quad G = C \\implies A + G = 50\\% N$$
2. **Chiều dài gen ($L$ tính bằng Angstrom $\\text{Å}$, $1\\text{ nm} = 10\\text{ Å}$):**
   $$L = \\frac{N}{2} \\times 3,4\\text{ Å}$$
3. **Số liên kết hydrogen ($H$):**
   $$H = 2A + 3G = 2T + 3C = N + G$$
4. **Sau $k$ lần tái bản từ 1 phân tử ADN ban đầu:**
   - Số phân tử ADN con tạo thành: $2^k$
   - Số phân tử ADN con giữ nguyên 1 mạch gốc cũ (bán bảo tồn): $2$
   - Số phân tử ADN cấu tạo hoàn toàn từ nguyên liệu môi trường: $2^k - 2$
   - Số nucleotide môi trường cung cấp:
     $$N_{\\text{mt}} = N \\times (2^k - 1)$$
     $$A_{\\text{mt}} = T_{\\text{mt}} = A \\times (2^k - 1)$$
     $$G_{\\text{mt}} = C_{\\text{mt}} = G \\times (2^k - 1)$$
"""

# ==============================================================================
# 6. TIN HỌC 10 - BIẾN & TOÁN TỬ PYTHON
# ==============================================================================
TIN_HOC_10_PYTHON = """# 📌 Chủ Đề: Biến, Kiểu Dữ Liệu và Toán Tử Trong Python

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
$$\\text{BMI} = \\frac{m}{h^2}$$
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
"""

# Dict of files to replace with complete master content
FEATURED_FILES = {
    "Toan/Lop_12/Chuong_01_Ung_dung_dao_ham_khao_sat_va_ve_do_thi_ham_so/01_Tinh_don_dieu_cua_ham_so.md": TOAN_12_DON_DIEU,
    "Vat_Ly/Lop_11/Chuong_01_Dao_dong/01_Dao_dong_dieu_hoa.md": VAT_LY_11_DAO_DONG,
    "Hoa_Hoc/Lop_12/Chuong_01_Ester_Lipid_Xa_phong/01_Ester.md": HOA_HOC_12_ESTER,
    "Toan/Lop_10/Chuong_04_Vecto/01_Khai_niem_vecto.md": TOAN_10_VECTO,
    "Sinh_Hoc/Lop_12/Chuong_01_Di_truyen_phan_tu/01_Gen_ma_di_truyen_tai_ban_ADN.md": SINH_HOC_12_ADN,
    "Tin_Hoc/Lop_10/Chuong_02_Lap_trinh_Python_co_ban/01_Bien_kieu_du_lieu_toan_tu.md": TIN_HOC_10_PYTHON
}

def main():
    for rel_path, content in FEATURED_FILES.items():
        abs_path = os.path.join(".", rel_path)
        write_file(abs_path, content)
    print("Populated all featured topics successfully!")

if __name__ == "__main__":
    main()
