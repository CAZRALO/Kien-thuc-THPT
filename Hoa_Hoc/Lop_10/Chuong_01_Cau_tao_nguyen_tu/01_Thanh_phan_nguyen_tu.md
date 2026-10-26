# 📌 Chủ Đề: Thành Phần & Cấu Trúc Nguyên Tử

> **Chương trình:** Hóa Học 10 (GDPT 2018)  
> **Chương I:** Cấu tạo nguyên tử  
> **Mức độ:** Cơ bản - Nâng cao

---

## 🎯 Mục Tiêu Bài Học
- Mô tả được thành phần của nguyên tử gồm hạt nhân (proton, neutron) và vỏ nguyên tử (electron).
- Nắm vững các thông số về điện tích, khối lượng của các loại hạt sơ cấp cấu thành nguyên tử.
- Viết đúng kí hiệu nguyên tử $_Z^A\text{X}$, hiểu khái niệm số hiệu nguyên tử $Z$, số khối $A$.
- Tính khối lượng nguyên tử tương đối theo đơn vị $amu$ và khối lượng thực tế tính bằng gam.

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Thành phần nguyên tử

Nguyên tử là hạt vô cùng nhỏ bé và **trung hoà về điện**, gồm 2 phần:
1. **Hạt nhân ở tâm:** Mang điện tích dương ($+Z$), kích thước rất nhỏ so với kích thước nguyên tử, gồm các hạt:
   - **Proton ($p$):** Mang điện tích nguyên tố $+1$ ($+1,602 \times 10^{-19}\text{ C}$), khối lượng $\approx 1,0073\text{ amu}$.
   - **Neutron ($n$):** Không mang điện, khối lượng $\approx 1,0087\text{ amu}$.
2. **Lớp vỏ:** Chứa các hạt **electron ($e$)** chuyển động rất nhanh xung quanh hạt nhân:
   - **Electron ($e$):** Mang điện tích nguyên tố $-1$ ($-1,602 \times 10^{-19}\text{ C}$), khối lượng rất nhỏ $\approx 0,00055\text{ amu}$ (bằng khoảng $\frac{1}{1836}$ khối lượng proton).

Do nguyên tử trung hoà về điện:
$$\text{Số proton } (p) = \text{Số electron } (e) = Z$$

---

## 🔢 II. Bảng So Sánh Các Hạt Sơ Cấp Của Nguyên Tử

| Hạt Sơ Cấp | Kí Hiệu | Điện Tích Tuyệt Đối ($C$) | Điện Tích Tương Đối | Khối Lượng Tuyệt Đối ($g$) | Khối Lượng ($amu$) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Proton** | $p$ | $+1,602 \times 10^{-19}$ | $+1$ | $1,673 \times 10^{-24}$ | $\approx 1$ |
| **Neutron** | $n$ | $0$ | $0$ | $1,675 \times 10^{-24}$ | $\approx 1$ |
| **Electron** | $e$ | $-1,602 \times 10^{-19}$ | $-1$ | $9,109 \times 10^{-28}$ | $\approx 0,00055$ |

> [!NOTE]
> Khối lượng của vỏ electron rất nhỏ so với hạt nhân ($m_e \ll m_p, m_n$).  
> Do đó, **khối lượng nguyên tử tập trung hầu như hoàn toàn ở hạt nhân**:
> $$m_{\text{nguyên tử}} \approx m_{\text{hạt nhân}} = m_p + m_n$$

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
$$_{Z}^{A}\text{X}$$
Trong đó:
- $\text{X}$: Kí hiệu hoá học của nguyên tố.
- $Z$: Số hiệu nguyên tử (số đơn vị điện tích hạt nhân = số proton = số electron).
- $A$: Số khối của hạt nhân:
  $$A = Z + N$$
  *(với $N$ là số hạt neutron)*.

### Dạng bài tập kinh điển: Tìm số hạt $p, n, e$
Cho tổng số hạt trong nguyên tử là $S$:
$$2Z + N = S$$
Đối với các nguyên tố bền có $Z \le 82$:
$$1 \le \frac{N}{Z} \le 1,52 \iff \frac{S}{3,52} \le Z \le \frac{S}{3}$$
Từ đó chặn khoảng giá trị của $Z$ và tìm nghiệm nguyên thích hợp.
