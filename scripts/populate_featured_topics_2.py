# -*- coding: utf-8 -*-
"""
Script bổ sung nội dung bài học chuyên sâu cho Vật lí 12 Nhiệt học, Toán 12 Tích phân, Hóa 10 Nguyên tử
"""
import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written {path}")

# ==============================================================================
# VẬT LÍ 12 - NỘI NĂNG VÀ ĐỊNH LUẬT I NHIỆT ĐỘNG LỰC HỌC
# ==============================================================================
VAT_LY_12_NOI_NANG = """# 📌 Chủ Đề: Nội Năng & Định Luật I Nhiệt Động Lực Học

> **Chương trình:** Vật Lí 12 (GDPT 2018)  
> **Chương I:** Vật lí nhiệt  
> **Mức độ:** Nhận biết - Thông hiểu - Vận dụng

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa nội năng ($U$) là tổng động năng chuyển động nhiệt của các phân tử và thế năng tương tác giữa chúng.
- Nắm rõ 2 cách làm biến đổi nội năng: **Thực hiện công** ($A$) và **Truyền nhiệt** ($Q$).
- Phát biểu và viết biểu thức toán học của Định luật I Nhiệt động lực học: $\\Delta U = Q + A$.
- Nắm vững quy ước về dấu của $Q$ và $A$ trong hệ nhiệt động.
- Ứng dụng định luật I giải quyết các quá trình biến đổi trạng thái của chất khí lí tưởng.

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Khái niệm Nội Năng
Trong nhiệt động lực học, **nội năng** ($U$) của một vật là tổng động năng của chuyển động nhiệt hỗn loạn của các phân tử cấu tạo nên vật và thế năng tương tác giữa chúng:
$$U = E_{\\text{đ phân tử}} + E_{\\text{t tương tác}}$$

- Nội năng của một lượng khí lí tưởng chỉ phụ thuộc vào **nhiệt độ tuyệt đối** $T$ của khối khí: $U = f(T)$.
- Nội năng của khí thực phụ thuộc vào cả **nhiệt độ** $T$ và **thể tích** $V$: $U = f(T, V)$.

### 2. Các cách làm thay đổi nội năng
1. **Thực hiện công ($A$):** Có sự chuyển hoá từ dạng năng lượng khác (cơ năng) sang nội năng (ví dụ: cọ xát miếng kim loại, nén pittông trong xi lanh).
2. **Truyền nhiệt ($Q$):** Không có sự chuyển hoá năng lượng từ dạng này sang dạng khác, chỉ có sự truyền nội năng từ vật có nhiệt độ cao sang vật có nhiệt độ thấp hơn.

---

## 🔢 II. Định Luật I Nhiệt Động Lực Học

### 1. Biểu thức toán học
$$\\Delta U = Q + A$$
Trong đó:
- $\\Delta U = U_2 - U_1$: Độ biến thiên nội năng của hệ (Đơn vị: Joule, $\\text{J}$).
- $Q$: Nhiệt lượng mà hệ nhận hoặc toả ra (Đơn vị: $\\text{J}$).
- $A$: Công mà hệ nhận được từ ngoại lực hoặc sinh ra tác dụng lên môi trường ngoài (Đơn vị: $\\text{J}$).

### 2. Bảng quy ước dấu sống còn

| Đại Lượng | Dấu Dương ($> 0$) | Dấu Âm ($< 0$) |
|:---:|:---|:---|
| **$Q$** | $Q > 0$: Hệ **nhận** nhiệt lượng từ môi trường ngoài | $Q < 0$: Hệ **truyền (toả)** nhiệt lượng ra ngoài |
| **$A$** | $A > 0$: Hệ **nhận** công từ môi trường (khí bị nén) | $A < 0$: Hệ **thực hiện (sinh)** công lên ngoại vật (khí giãn nở) |
| **$\\Delta U$** | $\\Delta U > 0$: Nội năng của hệ **tăng** | $\\Delta U < 0$: Nội năng của hệ **giảm** |

---

## 📊 III. Hình Biểu Diễn Trực Quan (SVG & Mermaid)

### 1. Sơ đồ quy ước dấu trong Định luật I (SVG)

<div align="center">
<svg width="540" height="280" viewBox="0 0 540 280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-in" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#22c55e"/>
    </marker>
    <marker id="arrow-out" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#ef4444"/>
    </marker>
  </defs>

  <rect width="540" height="280" rx="12" fill="#0f172a" stroke="#334155" stroke-width="2"/>

  <!-- Center System Box -->
  <rect x="180" y="80" width="180" height="120" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
  <text x="270" y="130" fill="#38bdf8" font-size="16" font-weight="bold" text-anchor="middle">HỆ NHIỆT ĐỘNG</text>
  <text x="270" y="155" fill="#e2e8f0" font-size="15" text-anchor="middle">ΔU = Q + A</text>

  <!-- Heat In (Q > 0) -->
  <line x1="60" y1="100" x2="170" y2="100" stroke="#22c55e" stroke-width="3" marker-end="url(#arrow-in)"/>
  <text x="110" y="90" fill="#22c55e" font-size="12" font-weight="bold" text-anchor="middle">Q &gt; 0 (Nhận nhiệt)</text>

  <!-- Heat Out (Q < 0) -->
  <line x1="170" y1="170" x2="60" y2="170" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow-out)"/>
  <text x="110" y="195" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">Q &lt; 0 (Toả nhiệt)</text>

  <!-- Work In (A > 0) -->
  <line x1="480" y1="100" x2="370" y2="100" stroke="#22c55e" stroke-width="3" marker-end="url(#arrow-in)"/>
  <text x="430" y="90" fill="#22c55e" font-size="12" font-weight="bold" text-anchor="middle">A &gt; 0 (Nhận công)</text>

  <!-- Work Out (A < 0) -->
  <line x1="370" y1="170" x2="480" y2="170" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow-out)"/>
  <text x="430" y="195" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">A &lt; 0 (Sinh công)</text>

  <text x="270" y="245" fill="#94a3b8" font-size="12" text-anchor="middle">Năng lượng đi VÀO: mang dấu (+) | Năng lượng đi RA: mang dấu (-)</text>
</svg>
<br>
<em>Hình 1.1: Quy tắc xác định dấu của năng lượng trong Định luật I</em>
</div>

---

## 💡 IV. Các Trường Hợp Riêng Cho Các Đẳng Quá Trình Của Khí Lí Tưởng

1. **Quá trình Đẳng tích ($V = \\text{const}$):**
   - Do thể tích không đổi nên khí không sinh công hay nhận công: $A = 0$.
   - Khi đó:
     $$\\Delta U = Q$$
   *(Độ biến thiên nội năng bằng toàn bộ nhiệt lượng mà khối khí nhận hay toả)*.

2. **Quá trình Đẳng nhiệt ($T = \\text{const}$):**
   - Với khí lí tưởng, nội năng chỉ phụ thuộc vào nhiệt độ. Vì $T$ không đổi nên $\\Delta U = 0$.
   - Khi đó:
     $$Q + A = 0 \\implies Q = -A = A'$$
   *(Nhiệt lượng khối khí nhận vào chuyển hoá toàn bộ thành công sinh ra cho ngoại vật $A'$)*.

3. **Quá trình Đoạn nhiệt (Cách nhiệt hoàn toàn với bên ngoài, $Q = 0$):**
   - Khối khí không trao đổi nhiệt với môi trường: $Q = 0$.
   - Khi đó:
     $$\\Delta U = A$$
   *(Nếu bị nén $A > 0 \\implies \\Delta U > 0$, nhiệt độ khối khí tăng lên)*.

---

## 📝 V. Ví Dụ Minh Họa Có Lời Giải Chi Tiết

**Đề bài:** Một khối khí lí tưởng chứa trong xi lanh có pittông đóng kín. Người ta cung cấp cho khối khí một nhiệt lượng $150\\text{ J}$. Đồng thời khối khí giãn nở và thực hiện một công $90\\text{ J}$ đẩy pittông đi lên. Tính độ biến thiên nội năng của khối khí.

**Lời giải:**
- Khối khí nhận nhiệt lượng từ bên ngoài nên:
  $$Q = +150\\text{ J}$$
- Khối khí thực hiện công (sinh công) lên pittông nên:
  $$A = -90\\text{ J}$$
- Áp dụng Định luật I Nhiệt động lực học:
  $$\\Delta U = Q + A = 150 + (-90) = +60\\text{ J}$$
- **Kết luận:** Nội năng của khối khí tăng thêm $60\\text{ J}$.
"""

# ==============================================================================
# TOÁN 12 - NGUYÊN HÀM & TÍNH CHẤT
# ==============================================================================
TOAN_12_NGUYEN_HAM = """# 📌 Chủ Đề: Nguyên Hàm và Các Tính Chất Cơ Bản

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
$$F'(x) = f(x), \\quad \\forall x \\in K$$

### 2. Định lý về họ nguyên hàm
Nếu $F(x)$ là một nguyên hàm của $f(x)$ trên $K$ thì:
- Mọi nguyên hàm của $f(x)$ trên $K$ đều có dạng:
  $$\\int f(x) \\, dx = F(x) + C \\quad (C \\in \\mathbb{R})$$

### 3. Các tính chất cơ bản
1. $\\left(\\int f(x) \\, dx\\right)' = f(x)$ và $\\int f'(x) \\, dx = f(x) + C$.
2. $\\int k \\cdot f(x) \\, dx = k \\int f(x) \\, dx$ *(với hằng số $k \\ne 0$)*.
3. $\\int [f(x) \\pm g(x)] \\, dx = \\int f(x) \\, dx \\pm \\int g(x) \\, dx$.

---

## 🔢 II. Bảng Nguyên Hàm Sơ Cấp & Mở Rộng

| Hàm Cơ Bản $\\int f(x) \\, dx$ | Nguyên Hàm Mở Rộng $\\int f(ax + b) \\, dx$ $(a \\ne 0)$ |
|:---|:---|
| $\\int 0 \\, dx = C$ | |
| $\\int dx = x + C$ | $\\int dx = x + C$ |
| $\\int x^\\alpha \\, dx = \\frac{x^{\\alpha + 1}}{\\alpha + 1} + C$ $(\\alpha \\ne -1)$ | $\\int (ax + b)^\\alpha \\, dx = \\frac{1}{a} \\cdot \\frac{(ax + b)^{\\alpha + 1}}{\\alpha + 1} + C$ |
| $\\int \\frac{1}{x} \\, dx = \\ln|x| + C$ | $\\int \\frac{1}{ax + b} \\, dx = \\frac{1}{a} \\ln|ax + b| + C$ |
| $\\int e^x \\, dx = e^x + C$ | $\\int e^{ax + b} \\, dx = \\frac{1}{a} e^{ax + b} + C$ |
| $\\int a^x \\, dx = \\frac{a^x}{\\ln a} + C$ $(0 < a \\ne 1)$ | $\\int a^{mx + n} \\, dx = \\frac{1}{m} \\cdot \\frac{a^{mx + n}}{\\ln a} + C$ |
| $\\int \\cos x \\, dx = \\sin x + C$ | $\\int \\cos(ax + b) \\, dx = \\frac{1}{a} \\sin(ax + b) + C$ |
| $\\int \\sin x \\, dx = -\\cos x + C$ | $\\int \\sin(ax + b) \\, dx = -\\frac{1}{a} \\cos(ax + b) + C$ |
| $\\int \\frac{1}{\\cos^2 x} \\, dx = \\tan x + C$ | $\\int \\frac{1}{\\cos^2(ax + b)} \\, dx = \\frac{1}{a} \\tan(ax + b) + C$ |
| $\\int \\frac{1}{\\sin^2 x} \\, dx = -\\cot x + C$ | $\\int \\frac{1}{\\sin^2(ax + b)} \\, dx = -\\frac{1}{a} \\cot(ax + b) + C$ |

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

**Ví dụ:** Tìm nguyên hàm $I = \\int (3x^2 - 4\\sin 2x + e^{3x}) \\, dx$.

**Lời giải:**
Áp dụng tính chất tuyến tính của nguyên hàm:
$$I = 3\\int x^2 \\, dx - 4\\int \\sin 2x \\, dx + \\int e^{3x} \\, dx$$
- Ta có:
  - $\\int x^2 \\, dx = \\frac{x^3}{3}$
  - $\\int \\sin 2x \\, dx = -\\frac{1}{2}\\cos 2x$
  - $\\int e^{3x} \\, dx = \\frac{1}{3}e^{3x}$
- Thay vào biểu thức $I$:
  $$I = 3 \\cdot \\frac{x^3}{3} - 4 \\left(-\\frac{1}{2}\\cos 2x\\right) + \\frac{1}{3}e^{3x} + C$$
  $$I = x^3 + 2\\cos 2x + \\frac{1}{3}e^{3x} + C$$
"""

# ==============================================================================
# HOÁ HỌC 10 - THÀNH PHẦN NGUYÊN TỬ
# ==============================================================================
HOA_HOC_10_NGUYEN_TU = """# 📌 Chủ Đề: Thành Phần & Cấu Trúc Nguyên Tử

> **Chương trình:** Hóa Học 10 (GDPT 2018)  
> **Chương I:** Cấu tạo nguyên tử  
> **Mức độ:** Cơ bản - Nâng cao

---

## 🎯 Mục Tiêu Bài Học
- Mô tả được thành phần của nguyên tử gồm hạt nhân (proton, neutron) và vỏ nguyên tử (electron).
- Nắm vững các thông số về điện tích, khối lượng của các loại hạt sơ cấp cấu thành nguyên tử.
- Viết đúng kí hiệu nguyên tử $_Z^A\\text{X}$, hiểu khái niệm số hiệu nguyên tử $Z$, số khối $A$.
- Tính khối lượng nguyên tử tương đối theo đơn vị $amu$ và khối lượng thực tế tính bằng gam.

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Thành phần nguyên tử

Nguyên tử là hạt vô cùng nhỏ bé và **trung hoà về điện**, gồm 2 phần:
1. **Hạt nhân ở tâm:** Mang điện tích dương ($+Z$), kích thước rất nhỏ so với kích thước nguyên tử, gồm các hạt:
   - **Proton ($p$):** Mang điện tích nguyên tố $+1$ ($+1,602 \\times 10^{-19}\\text{ C}$), khối lượng $\\approx 1,0073\\text{ amu}$.
   - **Neutron ($n$):** Không mang điện, khối lượng $\\approx 1,0087\\text{ amu}$.
2. **Lớp vỏ:** Chứa các hạt **electron ($e$)** chuyển động rất nhanh xung quanh hạt nhân:
   - **Electron ($e$):** Mang điện tích nguyên tố $-1$ ($-1,602 \\times 10^{-19}\\text{ C}$), khối lượng rất nhỏ $\\approx 0,00055\\text{ amu}$ (bằng khoảng $\\frac{1}{1836}$ khối lượng proton).

Do nguyên tử trung hoà về điện:
$$\\text{Số proton } (p) = \\text{Số electron } (e) = Z$$

---

## 🔢 II. Bảng So Sánh Các Hạt Sơ Cấp Của Nguyên Tử

| Hạt Sơ Cấp | Kí Hiệu | Điện Tích Tuyệt Đối ($C$) | Điện Tích Tương Đối | Khối Lượng Tuyệt Đối ($g$) | Khối Lượng ($amu$) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Proton** | $p$ | $+1,602 \\times 10^{-19}$ | $+1$ | $1,673 \\times 10^{-24}$ | $\\approx 1$ |
| **Neutron** | $n$ | $0$ | $0$ | $1,675 \\times 10^{-24}$ | $\\approx 1$ |
| **Electron** | $e$ | $-1,602 \\times 10^{-19}$ | $-1$ | $9,109 \\times 10^{-28}$ | $\\approx 0,00055$ |

> [!NOTE]
> Khối lượng của vỏ electron rất nhỏ so với hạt nhân ($m_e \\ll m_p, m_n$).  
> Do đó, **khối lượng nguyên tử tập trung hầu như hoàn toàn ở hạt nhân**:
> $$m_{\\text{nguyên tử}} \\approx m_{\\text{hạt nhân}} = m_p + m_n$$

---

## 📊 III. Hình Biểu Diễn Cấu Tạo Nguyên Tử (SVG)

<div align="center">
<svg width="460" height="300" viewBox="0 0 460 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="460" height="300" rx="12" fill="#0f172a" stroke="#334155" stroke-width="2"/>

  <!-- Orbits -->
  <ellipse cx="230" cy="150" rx="160" ry="60" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="4" transform="rotate(0, 230, 150)"/>
  <ellipse cx="230" cy="150" rx="160" ry="60" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="4" transform="rotate(60, 230, 150)"/>
  <ellipse cx="230" cy="150" rx="160" ry="60" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="4" transform="rotate(-60, 230, 150)"/>

  <!-- Nucleus -->
  <circle cx="230" cy="150" r="32" fill="#1e293b" stroke="#e11d48" stroke-width="2.5"/>
  <!-- Nucleon circles -->
  <circle cx="220" cy="142" r="10" fill="#ef4444"/>
  <text x="220" y="146" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">p+</text>
  <circle cx="240" cy="145" r="10" fill="#64748b"/>
  <text x="240" y="149" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">n</text>
  <circle cx="230" cy="160" r="10" fill="#ef4444"/>
  <text x="230" y="164" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">p+</text>

  <!-- Electrons on orbits -->
  <circle cx="390" cy="150" r="6" fill="#38bdf8"/>
  <text x="402" y="154" fill="#38bdf8" font-size="11" font-weight="bold">e-</text>

  <circle cx="150" cy="98" r="6" fill="#38bdf8"/>
  <circle cx="310" cy="202" r="6" fill="#38bdf8"/>

  <!-- Labels -->
  <text x="230" y="35" fill="#f8fafc" font-size="15" font-weight="bold" text-anchor="middle">Mô Hình Cấu Trúc Nguyên Tử</text>
  <text x="70" y="270" fill="#ef4444" font-size="12">● Proton (+)</text>
  <text x="180" y="270" fill="#64748b" font-size="12">● Neutron (0)</text>
  <text x="290" y="270" fill="#38bdf8" font-size="12">● Electron (-)</text>
</svg>
<br>
<em>Hình 1.1: Cấu tạo gồm hạt nhân (p, n) và các electron chuyển động xung quanh</em>
</div>

---

## 🔢 IV. Kí Hiệu Nguyên Tử & Hệ Phương Trình Hạt

Kí hiệu nguyên tử:
$$_{Z}^{A}\\text{X}$$
Trong đó:
- $\\text{X}$: Kí hiệu hoá học của nguyên tố.
- $Z$: Số hiệu nguyên tử (số đơn vị điện tích hạt nhân = số proton = số electron).
- $A$: Số khối của hạt nhân:
  $$A = Z + N$$
  *(với $N$ là số hạt neutron)*.

### Dạng bài tập kinh điển: Tìm số hạt $p, n, e$
Cho tổng số hạt trong nguyên tử là $S$:
$$2Z + N = S$$
Đối với các nguyên tố bền có $Z \\le 82$:
$$1 \\le \\frac{N}{Z} \\le 1,52 \\iff \\frac{S}{3,52} \\le Z \\le \\frac{S}{3}$$
Từ đó chặn khoảng giá trị của $Z$ và tìm nghiệm nguyên thích hợp.
"""

FILES = {
    "Vat_Ly/Lop_12/Chuong_01_Vat_ly_nhiet/02_Noi_nang_va_dinh_luat_I_nhiet_dong_luc_hoc.md": VAT_LY_12_NOI_NANG,
    "Toan/Lop_12/Chuong_04_Nguyen_ham_va_tich_phan/01_Nguyen_ham_va_tinh_chat.md": TOAN_12_NGUYEN_HAM,
    "Hoa_Hoc/Lop_10/Chuong_01_Cau_tao_nguyen_tu/01_Thanh_phan_nguyen_tu.md": HOA_HOC_10_NGUYEN_TU
}

def main():
    for rel_path, content in FILES.items():
        abs_path = os.path.join(".", rel_path)
        write_file(abs_path, content)
    print("Populated second batch of featured topics!")

if __name__ == "__main__":
    main()
