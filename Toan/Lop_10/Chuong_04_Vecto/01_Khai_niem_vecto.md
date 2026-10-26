# 📌 Chủ Đề: Khái Niệm Vectơ và Các Phép Toán Vectơ

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
- Kí hiệu: $\vec{a}, \vec{b}$ hoặc $\vec{AB}$ (điểm $A$ là điểm đầu, điểm $B$ là điểm cuối).
- Độ dài vectơ $\vec{AB}$ là khoảng cách giữa $A$ và $B$, kí hiệu $|\vec{AB}| = AB$.
- **Vectơ không** (kí hiệu $\vec{0}$): Là vectơ có điểm đầu và điểm cuối trùng nhau (ví dụ $\vec{AA}$). Độ dài bằng $0$, hướng tuỳ ý.

### 2. Hai vectơ cùng phương, cùng hướng
- Giá của vectơ: Đường thẳng đi qua điểm đầu và điểm cuối của vectơ đó.
- Hai vectơ gọi là **cùng phương** nếu giá của chúng song song hoặc trùng nhau.
- Nếu hai vectơ cùng phương thì chúng có thể **cùng hướng** hoặc **ngược hướng**.

---

## 🔢 II. Hệ Thống Các Quy Tắc Toán Học Vectơ

| Tên Quy Tắc | Biểu Thức Toán Học | Hình Minh Họa Ý Nghĩa |
|:---|:---|:---|
| **Quy tắc 3 điểm (Cộng nối tiếp)** | $\vec{AB} + \vec{BC} = \vec{AC}$ | Điểm cuối của vectơ này là điểm đầu của vectơ kia |
| **Quy tắc hiệu** | $\vec{AB} - \vec{AC} = \vec{CB}$ | Chung gốc $A$, lấy ngọn sau trừ ngọn trước |
| **Quy tắc hình bình hành** | $\vec{AB} + \vec{AD} = \vec{AC}$ | Với $ABCD$ là hình bình hành ($AC$ là đường chéo) |
| **Tính chất trung điểm $I$ của $AB$** | $\vec{IA} + \vec{IB} = \vec{0} \iff \vec{MA} + \vec{MB} = 2\vec{MI}$ | Đúng với mọi điểm $M$ bất kì |
| **Tính chất trọng tâm $G$ của $\Delta ABC$** | $\vec{GA} + \vec{GB} + \vec{GC} = \vec{0} \iff \vec{MA} + \vec{MB} + \vec{MC} = 3\vec{MG}$ | Đúng với mọi điểm $M$ bất kì |

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
$$\vec{AD} + \vec{BC} = 2\vec{MN}$$

**Lời giải chi tiết:**
- Theo quy tắc 3 điểm, ta chèn các điểm $M$ và $N$ vào hai vectơ ở vế trái:
  $$\vec{AD} = \vec{AM} + \vec{MN} + \vec{ND}$$
  $$\vec{BC} = \vec{BM} + \vec{MN} + \vec{NC}$$
- Cộng từng vế của hai đẳng thức trên, ta được:
  $$\vec{AD} + \vec{BC} = (\vec{AM} + \vec{BM}) + (\vec{MN} + \vec{MN}) + (\vec{ND} + \vec{NC})$$
- Vì $M$ là trung điểm của $AB$ nên $\vec{AM} + \vec{BM} = \vec{0}$.
- Vì $N$ là trung điểm của $CD$ nên $\vec{ND} + \vec{NC} = \vec{0}$.
- Do đó:
  $$\vec{AD} + \vec{BC} = \vec{0} + 2\vec{MN} + \vec{0} = 2\vec{MN} \quad \text{(Điều phải chứng minh)}$$
