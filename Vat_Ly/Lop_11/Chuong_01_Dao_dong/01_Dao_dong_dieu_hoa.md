# 📌 Chủ Đề: Dao Động Điều Hoà

> **Chương trình:** Vật Lí 11 (GDPT 2018)  
> **Chương I:** Dao động cơ học  
> **Mức độ:** Nhận biết - Thông hiểu - Vận dụng cao

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững định nghĩa dao động, dao động tuần hoàn và dao động điều hoà.
- Thuộc và hiểu ý nghĩa các đại lượng trong phương trình dao động điều hoà: li độ $x$, biên độ $A$, pha dao động $(\omega t + \varphi)$, tần số góc $\omega$, chu kì $T$, tần số $f$.
- Viết được phương trình vận tốc $v$, gia tốc $a$ và phân tích mối quan hệ lệch pha giữa $x$, $v$, $a$.
- Sử dụng thành thạo mối liên hệ giữa dao động điều hoà và chuyển động tròn đều qua vòng tròn lượng giác (VTLG).

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Khái niệm cơ bản
- **Dao động cơ:** Là chuyển động qua lại quanh một vị trí cân bằng (VTCB).
- **Dao động tuần hoàn:** Là dao động mà sau những khoảng thời gian bằng nhau gọi là chu kì, trạng thái dao động (vị trí, chiều và độ lớn vận tốc) của vật được lặp lại như cũ.
- **Dao động điều hoà:** Là dao động trong đó li độ của vật là một hàm côsin (hoặc sin) của thời gian.

### 2. Phương trình li độ
$$x = A \cos(\omega t + \varphi)$$
Trong đó:
- $x$: Li độ dao động (đơn vị: $cm$ hoặc $m$), khoảng cách đại số từ vật đến VTCB. $(-A \le x \le A)$
- $A$: Biên độ dao động ($A > 0$), là độ lệch cực đại của vật so với VTCB.
- $\omega$: Tần số góc (đơn vị: $rad/s$), $\omega > 0$.
- $(\omega t + \varphi)$: Pha của dao động tại thời điểm $t$ (đơn vị: $rad$), xác định trạng thái dao động.
- $\varphi$: Pha ban đầu tại thời điểm $t = 0$ (đơn vị: $rad$), thường quy ước $-\pi \le \varphi \le \pi$.

---

## 🔢 II. Hệ Thống Công Thức Cốt Lõi

### 1. Mối liên hệ chu kì, tần số và tần số góc
$$T = \frac{2\pi}{\omega} = \frac{1}{f} = \frac{\Delta t}{N} \quad \Longleftrightarrow \quad \omega = \frac{2\pi}{T} = 2\pi f$$
*(với $N$ là số dao động toàn phần thực hiện được trong thời gian $\Delta t$)*.

### 2. Bộ 3 phương trình chuyển động: Li độ - Vận tốc - Gia tốc

| Đại Lượng | Biểu Thức Tức Thời | Giá Trị Cực Đại (Max) | Giá Trị Cực Tiểu (Min) | Độ Lệch Pha So Với $x$ |
|:---|:---|:---|:---|:---|
| **Li độ** $x$ | $x = A\cos(\omega t + \varphi)$ | $x_{\max} = +A$ (Biên dương) | $x_{\min} = -A$ (Biên âm) | $0$ (Gốc chuẩn) |
| **Vận tốc** $v$ | $v = x' = -\omega A\sin(\omega t + \varphi) = \omega A\cos\left(\omega t + \varphi + \frac{\pi}{2}\right)$ | $v_{\max} = \omega A$ (Qua VTCB theo chiều dương) | $v_{\min} = -\omega A$ (Qua VTCB theo chiều âm) | Sớm pha $\frac{\pi}{2}$ (Vuông pha) |
| **Gia tốc** $a$ | $a = v' = -\omega^2 A\cos(\omega t + \varphi) = -\omega^2 x = \omega^2 A\cos(\omega t + \varphi + \pi)$ | $a_{\max} = \omega^2 A$ (Tại biên âm $x = -A$) | $a_{\min} = -\omega^2 A$ (Tại biên dương $x = +A$) | Sớm pha $\pi$ (Ngược pha) |

### 3. Hệ thức độc lập thời gian (Công thức vuông pha)
Do $x$ và $v$ vuông pha:
$$\left(\frac{x}{A}\right)^2 + \left(\frac{v}{\omega A}\right)^2 = 1 \implies A^2 = x^2 + \frac{v^2}{\omega^2} \implies v = \pm \omega \sqrt{A^2 - x^2}$$

Do $v$ và $a$ vuông pha:
$$\left(\frac{v}{v_{\max}}\right)^2 + \left(\frac{a}{a_{\max}}\right)^2 = 1 \implies \left(\frac{v}{\omega A}\right)^2 + \left(\frac{a}{\omega^2 A}\right)^2 = 1 \implies A^2 = \frac{v^2}{\omega^2} + \frac{a^2}{\omega^4}$$

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
- Đưa phương trình về dạng chuẩn $x = A\cos(\omega t + \varphi)$ với $A > 0$.
- Áp dụng các quy tắc biến đổi góc phụ và góc đối:
  - $-\cos(\alpha) = \cos(\alpha \pm \pi)$
  - $\sin(\alpha) = \cos\left(\alpha - \frac{\pi}{2}\right)$
  - $-\sin(\alpha) = \cos\left(\alpha + \frac{\pi}{2}\right)$

### Dạng 2: Ứng dụng vòng tròn lượng giác tìm thời gian ngắn nhất $\Delta t$
1. Xác định vị trí ban đầu $x_1$ và vị trí sau $x_2$ trên vòng tròn tương ứng với góc pha $\Phi_1, \Phi_2$.
2. Góc quét của vectơ quay: $\Delta \alpha = |\Phi_2 - \Phi_1|$ (tính bằng radian).
3. Thời gian quét:
   $$\Delta t = \frac{\Delta \alpha}{\omega} = \frac{\Delta \alpha}{2\pi} \cdot T$$

---

## 📝 V. Ví Dụ Minh Họa Có Lời Giải Chi Tiết

### Ví dụ 1:
**Đề bài:** Một vật dao động điều hoà có phương trình: $x = 4\cos\left(5\pi t - \frac{\pi}{3}\right)$ ($cm$).
1. Tìm biên độ, chu kì, tần số và tần số góc của dao động.
2. Viết phương trình vận tốc và gia tốc của vật.
3. Tính vận tốc và gia tốc của vật khi vật đi qua vị trí có li độ $x = 2\sqrt{3}$ $cm$ theo chiều âm.

**Lời giải chi tiết:**
1. **Các đại lượng đặc trưng:**
   - Biên độ: $A = 4\text{ cm}$.
   - Tần số góc: $\omega = 5\pi\text{ rad/s}$.
   - Chu kì: $T = \frac{2\pi}{\omega} = \frac{2\pi}{5\pi} = 0,4\text{ s}$.
   - Tần số: $f = \frac{1}{T} = 2,5\text{ Hz}$.

2. **Phương trình vận tốc và gia tốc:**
   - Phương trình vận tốc:
     $$v = x' = -20\pi \sin\left(5\pi t - \frac{\pi}{3}\right) = 20\pi \cos\left(5\pi t + \frac{\pi}{6}\right)\text{ (cm/s)}$$
   - Phương trình gia tốc:
     $$a = -\omega^2 x = -100\pi^2 \cos\left(5\pi t - \frac{\pi}{3}\right)\text{ (cm/s}^2\text{)}$$

3. **Tính $v$ và $a$ tại $x = 2\sqrt{3}$ cm theo chiều âm ($v < 0$):**
   - Áp dụng hệ thức độc lập:
     $$v = -\omega \sqrt{A^2 - x^2} = -5\pi \sqrt{4^2 - (2\sqrt{3})^2} = -5\pi \sqrt{16 - 12} = -10\pi\text{ cm/s}$$
   - Gia tốc tại thời điểm đó:
     $$a = -\omega^2 x = -(5\pi)^2 \cdot 2\sqrt{3} = -50\sqrt{3}\pi^2\text{ cm/s}^2 \approx -500\sqrt{3}\text{ cm/s}^2 \text{ (lấy } \pi^2 \approx 10\text{)}$$

---

## ⚡ VI. Bảng Ghi Nhớ Nhanh Các Khoảng Thời Gian Vàng

| Quãng Đường Chuyển Động | Góc Quét $\Delta \alpha$ | Thời Gian Tối Thiểu $\Delta t$ |
|:---|:---:|:---:|
| Từ $0 \to \frac{A}{2}$ hoặc $-\frac{A}{2} \to 0$ | $\frac{\pi}{6}$ | $\frac{T}{12}$ |
| Từ $\frac{A}{2} \to \frac{A\sqrt{2}}{2}$ | $\frac{\pi}{12}$ | $\frac{T}{24}$ |
| Từ $\frac{A\sqrt{2}}{2} \to \frac{A\sqrt{3}}{2}$ | $\frac{\pi}{12}$ | $\frac{T}{24}$ |
| Từ $\frac{A\sqrt{3}}{2} \to A$ | $\frac{\pi}{6}$ | $\frac{T}{12}$ |
| Từ $0 \to A$ | $\frac{\pi}{2}$ | $\frac{T}{4}$ |
| Từ $-A \to +A$ | $\pi$ | $\frac{T}{2}$ |
