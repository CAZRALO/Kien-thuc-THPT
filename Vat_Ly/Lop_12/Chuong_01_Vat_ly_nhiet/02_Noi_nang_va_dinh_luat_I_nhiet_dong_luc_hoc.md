# 📌 Chủ Đề: Nội Năng & Định Luật I Nhiệt Động Lực Học

> **Chương trình:** Vật Lí 12 (GDPT 2018)  
> **Chương I:** Vật lí nhiệt  
> **Mức độ:** Nhận biết - Thông hiểu - Vận dụng

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa nội năng ($U$) là tổng động năng chuyển động nhiệt của các phân tử và thế năng tương tác giữa chúng.
- Nắm rõ 2 cách làm biến đổi nội năng: **Thực hiện công** ($A$) và **Truyền nhiệt** ($Q$).
- Phát biểu và viết biểu thức toán học của Định luật I Nhiệt động lực học: $\Delta U = Q + A$.
- Nắm vững quy ước về dấu của $Q$ và $A$ trong hệ nhiệt động.
- Ứng dụng định luật I giải quyết các quá trình biến đổi trạng thái của chất khí lí tưởng.

---

## 📖 I. Lý Thuyết Trọng Tâm

### 1. Khái niệm Nội Năng
Trong nhiệt động lực học, **nội năng** ($U$) của một vật là tổng động năng của chuyển động nhiệt hỗn loạn của các phân tử cấu tạo nên vật và thế năng tương tác giữa chúng:
$$U = E_{\text{đ phân tử}} + E_{\text{t tương tác}}$$

- Nội năng của một lượng khí lí tưởng chỉ phụ thuộc vào **nhiệt độ tuyệt đối** $T$ của khối khí: $U = f(T)$.
- Nội năng của khí thực phụ thuộc vào cả **nhiệt độ** $T$ và **thể tích** $V$: $U = f(T, V)$.

### 2. Các cách làm thay đổi nội năng
1. **Thực hiện công ($A$):** Có sự chuyển hoá từ dạng năng lượng khác (cơ năng) sang nội năng (ví dụ: cọ xát miếng kim loại, nén pittông trong xi lanh).
2. **Truyền nhiệt ($Q$):** Không có sự chuyển hoá năng lượng từ dạng này sang dạng khác, chỉ có sự truyền nội năng từ vật có nhiệt độ cao sang vật có nhiệt độ thấp hơn.

---

## 🔢 II. Định Luật I Nhiệt Động Lực Học

### 1. Biểu thức toán học
$$\Delta U = Q + A$$
Trong đó:
- $\Delta U = U_2 - U_1$: Độ biến thiên nội năng của hệ (Đơn vị: Joule, $\text{J}$).
- $Q$: Nhiệt lượng mà hệ nhận hoặc toả ra (Đơn vị: $\text{J}$).
- $A$: Công mà hệ nhận được từ ngoại lực hoặc sinh ra tác dụng lên môi trường ngoài (Đơn vị: $\text{J}$).

### 2. Bảng quy ước dấu sống còn

| Đại Lượng | Dấu Dương ($> 0$) | Dấu Âm ($< 0$) |
|:---:|:---|:---|
| **$Q$** | $Q > 0$: Hệ **nhận** nhiệt lượng từ môi trường ngoài | $Q < 0$: Hệ **truyền (toả)** nhiệt lượng ra ngoài |
| **$A$** | $A > 0$: Hệ **nhận** công từ môi trường (khí bị nén) | $A < 0$: Hệ **thực hiện (sinh)** công lên ngoại vật (khí giãn nở) |
| **$\Delta U$** | $\Delta U > 0$: Nội năng của hệ **tăng** | $\Delta U < 0$: Nội năng của hệ **giảm** |

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

1. **Quá trình Đẳng tích ($V = \text{const}$):**
   - Do thể tích không đổi nên khí không sinh công hay nhận công: $A = 0$.
   - Khi đó:
     $$\Delta U = Q$$
   *(Độ biến thiên nội năng bằng toàn bộ nhiệt lượng mà khối khí nhận hay toả)*.

2. **Quá trình Đẳng nhiệt ($T = \text{const}$):**
   - Với khí lí tưởng, nội năng chỉ phụ thuộc vào nhiệt độ. Vì $T$ không đổi nên $\Delta U = 0$.
   - Khi đó:
     $$Q + A = 0 \implies Q = -A = A'$$
   *(Nhiệt lượng khối khí nhận vào chuyển hoá toàn bộ thành công sinh ra cho ngoại vật $A'$)*.

3. **Quá trình Đoạn nhiệt (Cách nhiệt hoàn toàn với bên ngoài, $Q = 0$):**
   - Khối khí không trao đổi nhiệt với môi trường: $Q = 0$.
   - Khi đó:
     $$\Delta U = A$$
   *(Nếu bị nén $A > 0 \implies \Delta U > 0$, nhiệt độ khối khí tăng lên)*.

---

## 📝 V. Ví Dụ Minh Họa Có Lời Giải Chi Tiết

**Đề bài:** Một khối khí lí tưởng chứa trong xi lanh có pittông đóng kín. Người ta cung cấp cho khối khí một nhiệt lượng $150\text{ J}$. Đồng thời khối khí giãn nở và thực hiện một công $90\text{ J}$ đẩy pittông đi lên. Tính độ biến thiên nội năng của khối khí.

**Lời giải:**
- Khối khí nhận nhiệt lượng từ bên ngoài nên:
  $$Q = +150\text{ J}$$
- Khối khí thực hiện công (sinh công) lên pittông nên:
  $$A = -90\text{ J}$$
- Áp dụng Định luật I Nhiệt động lực học:
  $$\Delta U = Q + A = 150 + (-90) = +60\text{ J}$$
- **Kết luận:** Nội năng của khối khí tăng thêm $60\text{ J}$.
