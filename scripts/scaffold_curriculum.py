# -*- coding: utf-8 -*-
"""
Script khởi tạo toàn bộ cấu trúc thư mục và nội dung mẫu chuẩn kiến thức THPT
Chương trình GDPT 2018 mới nhất
"""
import os
import json

CURRICULUM_DATA = {
    "Toan": {
        "name": "Toán Học",
        "icon": "📐",
        "description": "Hệ thống kiến thức Toán học THPT (Lớp 10, 11, 12): Đại số, Giải tích, Hình học, Xác suất & Thống kê",
        "grades": {
            "Lop_10": {
                "name": "Toán Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Menh_de_va_tap_hop",
                        "title": "Chương I: Mệnh Đề và Tập Hợp",
                        "topics": [
                            ("01_Menh_de_toan_hoc.md", "Mệnh đề toán học, phủ định, kéo theo, tương đương"),
                            ("02_Tap_hop_va_cac_phep_toan.md", "Tập hợp và các phép toán giao, hợp, hiệu, phần bù")
                        ]
                    },
                    {
                        "id": "Chuong_02_Bat_phuong_trinh_he_bat_phuong_trinh_bac_nhat_hai_an",
                        "title": "Chương II: Bất Phương Trình và Hệ Bất Phương Trình Bậc Nhất Hai Ẩn",
                        "topics": [
                            ("01_Bat_phuong_trinh_bac_nhat_hai_an.md", "Bất phương trình bậc nhất hai ẩn và miền nghiệm"),
                            ("02_He_bat_phuong_trinh_bac_nhat_hai_an.md", "Hệ bất phương trình bậc nhất hai ẩn và bài toán tối ưu F(x, y)")
                        ]
                    },
                    {
                        "id": "Chuong_03_He_thuc_luong_trong_tam_giac",
                        "title": "Chương III: Hệ Thức Lượng Trong Tam Giác",
                        "topics": [
                            ("01_Gia_tri_luong_giac_cua_mot_goc.md", "Giá trị lượng giác của góc từ 0 độ đến 180 độ"),
                            ("02_Dinh_li_cosin_va_dinh_li_sin.md", "Định lí côsin, định lí sin và các công thức tính diện tích tam giác"),
                            ("03_Giai_tam_giac_va_ung_dung_thuc_te.md", "Giải tam giác và ứng dụng đo đạc khoảng cách thực tế")
                        ]
                    },
                    {
                        "id": "Chuong_04_Vecto",
                        "title": "Chương IV: Vectơ và Các Phép Toán",
                        "topics": [
                            ("01_Khai_niem_vecto.md", "Khái niệm vectơ, vectơ cùng phương, cùng hướng, độ dài vectơ"),
                            ("02_Tong_va_hieu_cua_hai_vecto.md", "Tổng và hiệu hai vectơ, quy tắc ba điểm, quy tắc hình bình hành"),
                            ("03_Tich_cua_mot_so_voi_vecto.md", "Tích của một số với vectơ, điều kiện ba điểm thẳng hàng, trung điểm, trọng tâm"),
                            ("04_Tich_vo_huong_cua_hai_vecto.md", "Tích vô hướng, góc giữa hai vectơ, biểu thức toạ độ tích vô hướng")
                        ]
                    },
                    {
                        "id": "Chuong_05_Cac_so_dac_trung_do_xu_the_trung_tam",
                        "title": "Chương V: Các Số Đặc Trưng Đo Xu Thế Trung Tâm và Mức Độ Phân Tán",
                        "topics": [
                            ("01_So_gan_dung_va_sai_so.md", "Số gần đúng, sai số tuyệt đối, sai số tương đối, chữ số đáng tin"),
                            ("02_Cac_so_dac_trung_do_xu_the_trung_tam.md", "Số trung bình, trung vị, tứ phân vị, mốt"),
                            ("03_Cac_so_dac_trung_do_muc_do_phan_tan.md", "Khoảng biến thiên, khoảng tứ phân vị, phương sai, độ lệch chuẩn")
                        ]
                    },
                    {
                        "id": "Chuong_06_Ham_so_do_thi_va_ung_dung",
                        "title": "Chương VI: Hàm Số, Đồ Thị và Ứng Dụng",
                        "topics": [
                            ("01_Ham_so_va_do_thi.md", "Hàm số, tập xác định, tính đơn điệu, đồ thị"),
                            ("02_Ham_so_bac_hai.md", "Hàm số bậc hai y = ax^2 + bx + c, đỉnh parabol, trục đối xứng, bảng biến thiên"),
                            ("03_Dau_cua_tam_thuc_bac_hai.md", "Định lí về dấu của tam thức bậc hai, bất phương trình bậc hai một ẩn")
                        ]
                    },
                    {
                        "id": "Chuong_07_Phuong_phap_toa_do_trong_mat_phang",
                        "title": "Chương VII: Phương Pháp Toạ Độ Trong Mặt Phẳng (Oxy)",
                        "topics": [
                            ("01_Toa_do_cua_vecto_va_diem.md", "Toạ độ của vectơ và điểm trong mặt phẳng Oxy"),
                            ("02_Phuong_trinh_duong_thang.md", "Véctơ chỉ phương, pháp tuyến, phương trình tham số, phương trình tổng quát"),
                            ("03_Vi_tri_tuong_doi_goc_khoang_cach.md", "Vị trí tương đối, góc giữa hai đường thẳng, khoảng cách từ một điểm đến đường thẳng"),
                            ("04_Duong_tron_trong_mat_phang.md", "Phương trình đường tròn, tiếp tuyến của đường tròn"),
                            ("05_Ba_duong_conic.md", "Elip (Ellipse), Hypebol (Hyperbola), Parabol và các ứng dụng")
                        ]
                    },
                    {
                        "id": "Chuong_08_Dai_so_to_hop",
                        "title": "Chương VIII: Đại Số Tổ Hợp",
                        "topics": [
                            ("01_Quy_tac_dem.md", "Quy tắc cộng, quy tắc nhân, sơ đồ cây"),
                            ("02_Hoan_vi_chinh_hop_to_hop.md", "Hoán vị P_n, Chỉnh hợp A_n^k, Tổ hợp C_n^k"),
                            ("03_Nhi_thuc_newton.md", "Khai triển nhị thức Newton cho luỹ thừa bậc 4, 5")
                        ]
                    },
                    {
                        "id": "Chuong_09_Xac_suat",
                        "title": "Chương IX: Xác Suất",
                        "topics": [
                            ("01_Bien_co_va_khong_gian_mau.md", "Không gian mẫu, biến cố, các phép toán trên biến cố"),
                            ("02_Xac_suat_co_dien.md", "Định nghĩa cổ điển của xác suất và các tính chất cơ bản")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Toán Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Ham_so_luong_giac_va_phuong_trinh_luong_giac",
                        "title": "Chương I: Hàm Số Lượng Giác và Phương Trình Lượng Giác",
                        "topics": [
                            ("01_Goc_luong_giac_va_gia_tri_luong_giac.md", "Góc lượng giác, đơn vị radian, công thức lượng giác cơ bản"),
                            ("02_Cong_thuc_luong_giac.md", "Công thức cộng, góc nhân đôi, biến đổi tích thành tổng, tổng thành tích"),
                            ("03_Ham_so_luong_giac.md", "Hàm số sin, cos, tan, cot (tập xác định, chu kì, đồ thị)"),
                            ("04_Phuong_trinh_luong_giac_co_ban.md", "Giải phương trình sin x = m, cos x = m, tan x = m, cot x = m")
                        ]
                    },
                    {
                        "id": "Chuong_02_Day_so_cap_so_cong_cap_so_nhan",
                        "title": "Chương II: Dãy Số - Cấp Số Cộng và Cấp Số Nhân",
                        "topics": [
                            ("01_Day_so.md", "Định nghĩa dãy số, dãy tăng, dãy giảm, dãy bị chặn"),
                            ("02_Cap_so_cong.md", "Công sai d, số hạng tổng quát u_n, tổng n số hạng đầu S_n"),
                            ("03_Cap_so_nhan.md", "Công bội q, số hạng tổng quát u_n, tổng n số hạng đầu S_n, cấp số nhân lùi vô hạn")
                        ]
                    },
                    {
                        "id": "Chuong_03_Cac_so_dac_trung_do_xu_the_trung_tam_mau_ghep_nhom",
                        "title": "Chương III: Các Số Đặc Trưng Đo Xu Thế Trung Tâm Của Mẫu Số Liệu Ghép Nhóm",
                        "topics": [
                            ("01_Mau_so_lieu_ghep_nhom.md", "Thu thập và ghép nhóm số liệu, giá trị đại diện"),
                            ("02_Cac_so_dac_trung_mau_ghep_nhom.md", "Số trung bình, trung vị, tứ phân vị, mốt của mẫu ghép nhóm")
                        ]
                    },
                    {
                        "id": "Chuong_04_Quan_he_song_song_trong_khong_gian",
                        "title": "Chương IV: Quan Hệ Song Song Trong Không Gian",
                        "topics": [
                            ("01_Diem_duong_thang_mat_phang.md", "Các tính chất thừa nhận, điều kiện xác định mặt phẳng"),
                            ("02_Hai_duong_thang_song_song.md", "Vị trí tương đối của hai đường thẳng trong không gian"),
                            ("03_Duong_thang_song_song_voi_mat_phang.md", "Dấu hiệu nhận biết và tính chất đường thẳng song song với mặt phẳng"),
                            ("04_Hai_mat_phang_song_song.md", "Dấu hiệu nhận biết và tính chất hai mặt phẳng song song, hình lăng trụ, hình chóp cụt"),
                            ("05_Phep_chieu_song_song.md", "Định nghĩa phép chiếu song song và hình biểu diễn")
                        ]
                    },
                    {
                        "id": "Chuong_05_Gioi_han_ham_so_lien_tuc",
                        "title": "Chương V: Giới Hạn và Hàm Số Liên Tục",
                        "topics": [
                            ("01_Gioi_han_cua_day_so.md", "Giới hạn hữu hạn, vô cực, các định lí giới hạn dãy số"),
                            ("02_Gioi_han_cua_ham_so.md", "Giới hạn tại một điểm, tại vô cực, một bên, các dạng vô định"),
                            ("03_Ham_so_lien_tuc.md", "Hàm số liên tục tại một điểm, trên một khoảng, định lí Bolzano")
                        ]
                    },
                    {
                        "id": "Chuong_06_Ham_so_mu_va_ham_so_logarit",
                        "title": "Chương VI: Hàm Số Mũ và Hàm Số Lôgarit",
                        "topics": [
                            ("01_Phep_tinh_luy_thua.md", "Luỹ thừa với số mũ nguyên, hữu tỉ, thực"),
                            ("02_Phep_tinh_logarit.md", "Định nghĩa lôgarit, tính chất, đổi cơ số, logarit tự nhiên ln"),
                            ("03_Ham_so_mu_va_logarit.md", "Định nghĩa, tính chất, tập xác định, đồ thị của hàm số y = a^x và y = log_a(x)"),
                            ("04_Phuong_trinh_bat_phuong_trinh_mu_logarit.md", "Phương pháp giải phương trình, bất phương trình mũ và logarit")
                        ]
                    },
                    {
                        "id": "Chuong_07_Dao_ham",
                        "title": "Chương VII: Đạo Hàm",
                        "topics": [
                            ("01_Dinh_nghia_va_y_nghia_dao_ham.md", "Định nghĩa đạo hàm, ý nghĩa hình học (tiếp tuyến), ý nghĩa vật lí"),
                            ("02_Quy_tac_tinh_dao_ham.md", "Bảng đạo hàm cơ bản, đạo hàm hàm hợp, quy tắc tổng hiệu tích thương"),
                            ("03_Dao_ham_cap_hai.md", "Đạo hàm cấp hai và ý nghĩa gia tốc trong chuyển động")
                        ]
                    },
                    {
                        "id": "Chuong_08_Quan_he_vuong_goc_trong_khong_gian",
                        "title": "Chương VIII: Quan Hệ Vuông Góc Trong Không Gian",
                        "topics": [
                            ("01_Hai_duong_thang_vuong_goc.md", "Góc giữa hai đường thẳng, hai đường thẳng vuông góc"),
                            ("02_Duong_thang_vuong_goc_voi_mat_phang.md", "Điều kiện đường thẳng vuông góc mặt phẳng, định lí ba đường vuông góc"),
                            ("03_Hai_mat_phang_vuong_goc.md", "Góc giữa hai mặt phẳng, diện tích hình chiếu, hình lăng trụ đứng, hình chóp đều"),
                            ("04_Khoang_cach_trong_khong_gian.md", "Khoảng cách từ điểm đến đường thẳng, mặt phẳng, khoảng cách giữa hai đường chéo nhau"),
                            ("05_The_tich_khoi_da_dien.md", "Thể tích khối lăng trụ, khối chóp, khối hộp")
                        ]
                    },
                    {
                        "id": "Chuong_09_Xac_suat",
                        "title": "Chương IX: Xác Suất",
                        "topics": [
                            ("01_Bien_co_giao_va_bien_co_doc_lap.md", "Biến cố hợp, biến cố giao, hai biến cố xung khắc, độc lập"),
                            ("02_Quy_tac_cong_va_nhan_xac_suat.md", "Công thức cộng xác suất, công thức nhân xác suất cho biến cố độc lập")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Toán Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Ung_dung_dao_ham_khao_sat_va_ve_do_thi_ham_so",
                        "title": "Chương I: Ứng Dụng Đạo Hàm Khảo Sát và Vẽ Đồ Thị Hàm Số",
                        "topics": [
                            ("01_Tinh_don_dieu_cua_ham_so.md", "Định lí dấu đạo hàm bậc nhất, xét tính đồng biến, nghịch biến"),
                            ("02_Cuc_tri_cua_ham_so.md", "Điều kiện cần và đủ cực trị, quy tắc 1, quy tắc 2"),
                            ("03_Gia_tri_lon_nhat_va_nho_nhat.md", "Tìm GTLN và GTNN trên đoạn [a, b], trên khoảng mở"),
                            ("04_Duong_tiem_can_cua_do_thi.md", "Tiệm cận đứng, tiệm cận ngang, tiệm cận xiên"),
                            ("05_Khao_sat_su_bien_thien_va_ve_do_thi.md", "Sơ đồ khảo sát hàm bậc ba, hàm phân thức bậc nhất/bậc nhất, phân thức bậc hai/bậc nhất"),
                            ("06_Ung_dung_thuc_te_cua_dao_ham.md", "Bài toán tối ưu hoá trong kinh tế, kỹ thuật, đời sống")
                        ]
                    },
                    {
                        "id": "Chuong_02_Toa_do_vecto_trong_khong_gian_Oxyz",
                        "title": "Chương II: Toạ Độ Vectơ Trong Không Gian (Oxyz)",
                        "topics": [
                            ("01_He_truc_toa_do_trong_khong_gian.md", "Hệ trục Oxyz, toạ độ của điểm và toạ độ của vectơ"),
                            ("02_Bieu_thuc_toa_do_cac_phep_toan.md", "Tổng hiệu tích vectơ với số, toạ độ trung điểm, trọng tâm"),
                            ("03_Tich_vo_huong_va_ung_dung.md", "Biểu thức tích vô hướng, độ dài vectơ, góc giữa hai vectơ, khoảng cách hai điểm"),
                            ("04_Tich_co_huong_cua_hai_vecto.md", "Định nghĩa tích có hướng, diện tích tam giác, thể tích tứ diện")
                        ]
                    },
                    {
                        "id": "Chuong_03_Cac_so_dac_trung_do_muc_do_phan_tan_mau_ghep_nhom",
                        "title": "Chương III: Các Số Đặc Trưng Đo Mức Độ Phân Tán Mẫu Số Liệu Ghép Nhóm",
                        "topics": [
                            ("01_Khoang_bien_thien_va_khoang_tu_phan_vi.md", "Công thức tính khoảng biến thiên R và khoảng tứ phân vị Delta_Q"),
                            ("02_Phuong_sai_va_do_lech_chuan.md", "Công thức tính phương sai s^2 và độ lệch chuẩn s cho mẫu ghép nhóm")
                        ]
                    },
                    {
                        "id": "Chuong_04_Nguyen_ham_va_tich_phan",
                        "title": "Chương IV: Nguyên Hàm và Tích Phân",
                        "topics": [
                            ("01_Nguyen_ham_va_tinh_chat.md", "Khái niệm nguyên hàm, bảng nguyên hàm cơ bản và mở rộng"),
                            ("02_Cac_phuong_phap_tinh_nguyen_ham.md", "Phương pháp đổi biến số, phương pháp nguyên hàm từng phần"),
                            ("03_Tich_phan_va_dinh_nghia.md", "Định nghĩa tích phân theo Newton-Leibniz, các tính chất tích phân"),
                            ("04_Ung_dung_hinh_hoc_cua_tich_phan.md", "Tính diện tích hình phẳng giới hạn bởi các đường cong, thể tích khối tròn xoay")
                        ]
                    },
                    {
                        "id": "Chuong_05_Phuong_phap_toa_do_trong_khong_gian_Oxyz",
                        "title": "Chương V: Phương Pháp Toạ Độ Trong Không Gian (Oxyz)",
                        "topics": [
                            ("01_Phuong_trinh_mat_phang.md", "Vectơ pháp tuyến, phương trình tổng quát mặt phẳng, khoảng cách từ điểm đến mp"),
                            ("02_Phuong_trinh_duong_thang.md", "Vectơ chỉ phương, phương trình tham số, phương trình chính tắc của đường thẳng"),
                            ("03_Phuong_trinh_mat_cau.md", "Phương trình chính tắc mặt cầu tâm I(a,b,c) bán kính R, dạng khai triển"),
                            ("04_Vi_tri_tuong_doi_va_goc.md", "Vị trí tương đối điểm, đường, mặt; góc giữa hai đường thẳng, góc giữa đường và mặt")
                        ]
                    },
                    {
                        "id": "Chuong_06_Xac_suat_co_dieu_kien",
                        "title": "Chương VI: Xác Suất Có Điều Kiện",
                        "topics": [
                            ("01_Xac_suat_co_dieu_kien.md", "Khái niệm P(A|B), công thức nhân xác suất"),
                            ("02_Cong_thuc_xac_suat_toan_phan_va_Bayes.md", "Công thức xác suất toàn phần, công thức Bayes và ứng dụng chẩn đoán")
                        ]
                    }
                ]
            }
        }
    },
    "Vat_Ly": {
        "name": "Vật Lí",
        "icon": "⚡",
        "description": "Toàn bộ kiến thức Vật lí THPT (Lớp 10, 11, 12): Cơ học, Sóng, Điện từ trường, Nhiệt học, Khí lí tưởng, Vật lí hạt nhân",
        "grades": {
            "Lop_10": {
                "name": "Vật Lí Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Mo_dau",
                        "title": "Chương I: Mở Đầu và Sai Số Trong Thực Hành",
                        "topics": [
                            ("01_Khai_quat_mon_vat_ly.md", "Đối tượng nghiên cứu, phương pháp thực nghiệm và mô hình hoá"),
                            ("02_Sai_so_phep_do.md", "Sai số hệ thống, sai số ngẫu nhiên, cách viết kết quả đo")
                        ]
                    },
                    {
                        "id": "Chuong_02_Mo_ta_chuyen_dong",
                        "title": "Chương II: Động Học - Mô Tả Chuyển Động",
                        "topics": [
                            ("01_Do_dich_chuyen_va_quang_duong.md", "Độ dịch chuyển, phân biệt quãng đường và độ dịch chuyển"),
                            ("02_Toc_do_va_van_toc.md", "Tốc độ trung bình, vận tốc tức thời, đồ thị độ dịch chuyển - thời gian"),
                            ("03_Chuyen_dong_thang_bien_doi_deu.md", "Gia tốc, phương trình vận tốc, phương trình chuyển động, đồ thị v-t"),
                            ("04_Roi_tu_do_va_chuyen_dong_nem.md", "Sự rơi tự do, gia tốc trọng trường g, chuyển động ném ngang và ném xiên")
                        ]
                    },
                    {
                        "id": "Chuong_03_Dong_luc_hoc",
                        "title": "Chương III: Động Lực Học - Các Định Luật Newton",
                        "topics": [
                            ("01_Ba_dinh_luat_Newton.md", "Định luật I, II, III Newton, quán tính, khối lượng, lực và phản lực"),
                            ("02_Cac_luc_co_hoc.md", "Trọng lực, lực ma sát trượt/nghỉ, lực căng dây, lực đẩy Archimedes"),
                            ("03_Can_bang_va_momen_luc.md", "Quy tắc momen lực, điều kiện cân bằng của vật rắn quay quanh trục cố định")
                        ]
                    },
                    {
                        "id": "Chuong_04_Nang_luong_cong_cong_suat",
                        "title": "Chương IV: Năng Lượng - Công và Công Suất",
                        "topics": [
                            ("01_Cong_va_cong_suat.md", "Định nghĩa công cơ học A = F.s.cos(alpha), công suất P = A/t"),
                            ("02_Dong_nang_the_nang_co_nang.md", "Động năng, thế năng trọng trường, định luật bảo toàn cơ năng"),
                            ("03_Hieu_suat_va_hao_phi.md", "Năng lượng có ích, năng lượng toàn phần, công thức hiệu suất")
                        ]
                    },
                    {
                        "id": "Chuong_05_Dong_luong",
                        "title": "Chương V: Động Lượng và Định Luật Bảo Toàn Động Lượng",
                        "topics": [
                            ("01_Dong_luong_va_xung_luong.md", "Vectơ động lượng p = mv, độ biến thiên động lượng và xung lượng của lực"),
                            ("02_Dinh_luat_bao_toan_dong_luong.md", "Hệ kín, định luật bảo toàn động lượng, va chạm đàn hồi và va chạm mềm")
                        ]
                    },
                    {
                        "id": "Chuong_06_Chuyen_dong_tron",
                        "title": "Chương VI: Chuyển Động Tròn Đều",
                        "topics": [
                            ("01_Mo_ta_chuyen_dong_tron.md", "Tốc độ góc, chu kì T, tần số f, gia tốc hướng tâm a_ht = v^2/r"),
                            ("02_Luc_huong_tam.md", "Khái niệm lực hướng tâm F_ht = m.v^2/r và các ví dụ thực tế")
                        ]
                    },
                    {
                        "id": "Chuong_07_Bien_dang_vat_ran_va_ap_suat",
                        "title": "Chương VII: Biến Dạng Vật Rắn và Áp Suất Chất Lưu",
                        "topics": [
                            ("01_Bien_dang_co_cua_vat_ran.md", "Biến dạng đàn hồi, định luật Hooke F_dh = k.|delta l|"),
                            ("02_Ap_suat_chat_long_chat_khi.md", "Áp suất chất lỏng p = p0 + rho.g.h, nguyên lí Pascal")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Vật Lí Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Dao_dong",
                        "title": "Chương I: Dao Động Cơ Học",
                        "topics": [
                            ("01_Dao_dong_dieu_hoa.md", "Phương trình li độ x = A.cos(omega.t + phi), vận tốc, gia tốc"),
                            ("02_Mo_ta_dao_dong_dieu_hoa.md", "Đồ thị dao động điều hoà, mối liên hệ x, v, a theo pha"),
                            ("03_Nang_luong_trong_dao_dong_dieu_hoa.md", "Động năng, thế năng, cơ năng E = 1/2 m.omega^2.A^2"),
                            ("04_Dao_dong_tat_dan_cuong_buc_cong_huong.md", "Dao động tắt dần, dao động cưỡng bức, hiện tượng cộng hưởng cơ")
                        ]
                    },
                    {
                        "id": "Chuong_02_Song",
                        "title": "Chương II: Sóng Cơ và Sóng Âm",
                        "topics": [
                            ("01_Mo_ta_song_va_su_truyen_song.md", "Sóng dọc, sóng ngang, bước sóng lambda = v.T = v/f, phương trình sóng"),
                            ("02_Giao_thoa_song.md", "Điều kiện giao thoa, cực đại cực tiểu giao thoa, hình ảnh vân giao thoa"),
                            ("03_Song_dung.md", "Sự phản xạ sóng, nút sóng, bụng sóng, điều kiện có sóng dừng"),
                            ("04_Song_am.md", "Đặc trưng vật lí (tần số, mức cường độ âm L) và đặc trưng sinh lí của âm")
                        ]
                    },
                    {
                        "id": "Chuong_03_Dien_truong",
                        "title": "Chương III: Điện Trường",
                        "topics": [
                            ("01_Luc_tuong_tac_tinh_dien.md", "Định luật Coulomb F = k.|q1.q2| / (epsilon.r^2)"),
                            ("02_Cuong_do_dien_truong.md", "Định nghĩa vectơ E = F/q, điện trường của điện tích điểm, đường sức điện"),
                            ("03_Dien_the_va_the_nang_dien.md", "Công của lực điện trường, điện thế V, hiệu điện thế U = E.d"),
                            ("04_Tu_dien.md", "Điện dung của tụ điện C = Q/U, năng lượng điện trường trong tụ điện")
                        ]
                    },
                    {
                        "id": "Chuong_04_Dong_dien_khong_doi",
                        "title": "Chương IV: Dòng Điện Không Đổi",
                        "topics": [
                            ("01_Dong_dien_nguon_dien.md", "Cường độ dòng điện I = q/t, suất điện động E của nguồn điện"),
                            ("02_Dinh_luat_ohm_cho_toan_mach.md", "Định luật Ohm I = E / (R_N + r), hiện tượng đoản mạch"),
                            ("03_Nang_luong_va_cong_suat_dien.md", "Định luật Joule - Lenz, công và công suất của nguồn điện và mạch ngoài")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Vật Lí Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Vat_ly_nhiet",
                        "title": "Chương I: Vật Lí Nhiệt",
                        "topics": [
                            ("01_Cau_truc_chat_va_su_chuyen_the.md", "Mô hình cấu trúc chất rắn, lỏng, khí; sự nóng chảy, đông đặc, bay hơi, sôi"),
                            ("02_Noi_nang_va_dinh_luat_I_nhiet_dong_luc_hoc.md", "Nội năng, các cách làm thay đổi nội năng, định luật I nhiệt động lực học Delta U = Q + A"),
                            ("03_Nhiet_do_va_thang_nhiet_do.md", "Thang đo Celsius, Kelvin; mối liên hệ T(K) = t(°C) + 273.15"),
                            ("04_Nhiet_dung_rieng_nhiet_nong_chay_nhiet_hoa_hoi.md", "Công thức Q = mc.Delta t, Q = lambda.m, Q = L.m và thí nghiệm đo nhiệt lượng")
                        ]
                    },
                    {
                        "id": "Chuong_02_Khi_ly_tuong",
                        "title": "Chương II: Khí Lí Tưởng",
                        "topics": [
                            ("01_Mo_hinh_dong_hoc_phan_tu_chat_khi.md", "Các giả thuyết về khí lí tưởng, chuyển động hỗn loạn của phân tử"),
                            ("02_Cac_dinh_luat_chat_khi.md", "Định luật Boyle (đẳng nhiệt pV = const), định luật Charles (đẳng tích p/T = const)"),
                            ("03_Phuong_trinh_trang_thai_khi_ly_tuong.md", "Phương trình pV = nRT = (m/M)RT, phương trình Clapeyron - Mendeleev"),
                            ("04_Ap_suat_dong_hoc_va_dong_nang_phan_tu.md", "Công thức áp suất p = 1/3 rho.v^2, động năng trung bình phân tử E_d = 3/2 k.T")
                        ]
                    },
                    {
                        "id": "Chuong_03_Tu_truong",
                        "title": "Chương III: Từ Trường và Cảm Ứng Điện Từ",
                        "topics": [
                            ("01_Tu_truong_va_duong_suc_tu.md", "Tương tác từ, cảm ứng từ B, quy tắc nắm tay phải, đường sức từ"),
                            ("02_Luc_tu_va_luc_Lorentz.md", "Lực từ tác dụng lên đoạn dây dẫn mang dòng F = B.I.l.sin(alpha), lực Lorentz tác dụng lên điện tích chuyển động"),
                            ("03_Hien_tuong_cam_ung_dien_tu.md", "Từ thông Phi = B.S.cos(alpha), định luật Faraday về suất điện động cảm ứng, định luật Lenz"),
                            ("04_Hien_tuong_tu_cam.md", "Độ tự cảm L của ống dây, suất điện động tự cảm e_tc = -L.(Delta i / Delta t)")
                        ]
                    },
                    {
                        "id": "Chuong_04_Vat_ly_hat_nhan",
                        "title": "Chương IV: Vật Lí Hạt Nhân",
                        "topics": [
                            ("01_Cau_tao_hat_nhan_va_do_hut_khoi.md", "Proton, neutron, số khối A, hệ thức Einstein E = mc^2, độ hụt khối Delta m, năng lượng liên kết riêng"),
                            ("02_Phan_ung_hat_nhan.md", "Định luật bảo toàn điện tích, số khối, năng lượng trong phản ứng hạt nhân"),
                            ("03_Hien_tuong_phong_xa.md", "Các tia phóng xạ alpha, beta-, beta+, gamma; chu kì bán rã T, định luật phóng xạ"),
                            ("04_Phan_hach_nhiet_hach_ung_dung.md", "Phản ứng phân hạch U-235, phản ứng nhiệt hạch (tổng hợp), ứng dụng y học và năng lượng hạt nhân")
                        ]
                    }
                ]
            }
        }
    },
    "Hoa_Hoc": {
        "name": "Hóa Học",
        "icon": "🧪",
        "description": "Toàn diện Hóa học THPT: Cấu tạo nguyên tử, Bảng tuần hoàn, Liên kết hóa học, Nhiệt hóa học, Hóa học hữu cơ, Polymer, Pin điện & Kim loại",
        "grades": {
            "Lop_10": {
                "name": "Hóa Học Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Cau_tao_nguyen_tu",
                        "title": "Chương I: Cấu Tạo Nguyên Tử",
                        "topics": [
                            ("01_Thanh_phan_nguyen_tu.md", "Hạt proton, neutron, electron; kích thước và khối lượng nguyên tử"),
                            ("02_Hat_nhan_nguyen_to_dong_vi.md", "Số hiệu nguyên tử Z, số khối A, đồng vị và khối lượng nguyên tử trung bình"),
                            ("03_Cau_truc_lop_vo_electron.md", "Mô hình Rutherford-Bohr, mô hình hiện đại (orbital s, p, d, f), cấu hình electron")
                        ]
                    },
                    {
                        "id": "Chuong_02_Bang_tuan_hoan",
                        "title": "Chương II: Bảng Tuần Hoàn Các Nguyên Tố Hóa Học",
                        "topics": [
                            ("01_Cau_tao_bang_tuan_hoan.md", "Ô nguyên tố, chu kì, nhóm A, nhóm B"),
                            ("02_Xu_huong_bien_doi_tuan_hoan.md", "Bán kính nguyên tử, độ âm điện, tính kim loại/phi kim, tính acid/base")
                        ]
                    },
                    {
                        "id": "Chuong_03_Lien_ket_hoa_hoc",
                        "title": "Chương III: Liên Kết Hóa Học",
                        "topics": [
                            ("01_Quy_tac_octet_lien_ket_ion.md", "Quy tắc octet, sự hình thành ion và liên kết ion"),
                            ("02_Lien_ket_cong_hoa_tri.md", "Liên kết cộng hoá trị có cực/không cực, liên kết sigma và pi"),
                            ("03_Lien_ket_hydrogen_tuong_tac_van_der_waals.md", "Bản chất liên kết hydrogen, ảnh hưởng đến nhiệt độ sôi và độ tan")
                        ]
                    },
                    {
                        "id": "Chuong_04_Phan_ung_oxi_hoa_khu",
                        "title": "Chương IV: Phản Ứng Oxi Hóa - Khử",
                        "topics": [
                            ("01_So_oxi_hoa.md", "Quy tắc xác định số oxi hoá của các nguyên tố"),
                            ("02_Phan_ung_oxi_hoa_khu_va_can_bang.md", "Chất oxi hoá, chất khử, quá trình oxi hoá/khử, phương pháp thăng bằng electron")
                        ]
                    },
                    {
                        "id": "Chuong_05_Nang_luong_hoa_hoc",
                        "title": "Chương V: Năng Lượng Hóa Học",
                        "topics": [
                            ("01_Phan_ung_toa_nhiet_thu_nhiet.md", "Khái niệm enthalpy Delta_r H, phản ứng toả nhiệt và thu nhiệt"),
                            ("02_Tinh_bien_thien_enthalpy_phan_ung.md", "Tính Delta_r H^0 theo nhiệt tạo thành chuẩn và năng lượng liên kết E_b")
                        ]
                    },
                    {
                        "id": "Chuong_06_Toc_do_phan_ung",
                        "title": "Chương VI: Tốc Độ Phản Ứng Hóa Học",
                        "topics": [
                            ("01_Khai_niem_va_bieu_thuc_toc_do.md", "Tốc độ trung bình, định luật tác dụng khối lượng v = k.[A]^a.[B]^b"),
                            ("02_Cac_yeu_to_anh_huong_toc_do.md", "Nồng độ, nhiệt độ (hệ số Van't Hoff), áp suất, diện tích bề mặt, chất xúc tác")
                        ]
                    },
                    {
                        "id": "Chuong_07_Halogen",
                        "title": "Chương VII: Nguyên Tố Nhóm VIIA (Halogen)",
                        "topics": [
                            ("01_Don_chat_halogen.md", "Tính chất vật lí, tính chất hoá học (tính oxi hoá mạnh giảm dần F2 > Cl2 > Br2 > I2)"),
                            ("02_Hydrogen_halide_va_muoi_halide.md", "Tính acid của hydrohalic acid, nhận biết ion halide Cl-, Br-, I-")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Hóa Học Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Can_bang_hoa_hoc",
                        "title": "Chương I: Cân Bằng Hóa Học và Sự Điện Li",
                        "topics": [
                            ("01_Khai_niem_can_bang_hoa_hoc.md", "Phản ứng thuận nghịch, hằng số cân bằng K_c, nguyên lí chuyển dịch Le Chatelier"),
                            ("02_Can_bang_trong_dung_dich_nuoc.md", "Thuyết Brønsted - Lowry về acid/base, tích số ion của nước K_w, thang pH")
                        ]
                    },
                    {
                        "id": "Chuong_02_Nitrogen_va_Sulfur",
                        "title": "Chương II: Nitrogen và Sulfur",
                        "topics": [
                            ("01_Nitrogen_ammonia_muoi_ammonium.md", "Đơn chất N2, tính base và tính khử của NH3, ion NH4+"),
                            ("02_Nitric_acid_muoi_nitrate.md", "Tính acid mạnh và tính oxi hoá mạnh của HNO3"),
                            ("03_Sulfur_va_sulfur_dioxide.md", "Đơn chất S, tính oxi hoá và khử của SO2, mưa acid"),
                            ("04_Sulfuric_acid_va_muoi_sulfate.md", "Tính chất của H2SO4 đặc (háo nước, oxi hoá mạnh), nhận biết ion SO4^2-")
                        ]
                    },
                    {
                        "id": "Chuong_03_Dai_cuong_hoa_hoc_huu_co",
                        "title": "Chương III: Đại Cương Về Hóa Học Hữu Cơ",
                        "topics": [
                            ("01_Hop_chat_huu_co_va_nhom_chuc.md", "Đặc điểm cấu tạo hợp chất hữu cơ, phổ hồng ngoại IR và nhóm chức"),
                            ("02_Phuong_phap_tach_va_tinh_che.md", "Phương pháp chưng cất, chiết, kết tinh, sắc kí cột"),
                            ("03_Cong_thuc_phan_tu_va_dong_phan.md", "Xác định công thức đơn giản nhất, phổ khối lượng MS xác định M, đồng phân cấu tạo và hình học")
                        ]
                    },
                    {
                        "id": "Chuong_04_Hydrocarbon",
                        "title": "Chương IV: Hydrocarbon",
                        "topics": [
                            ("01_Alkane.md", "Công thức C_n H_{2n+2}, phản ứng thế halogen, cracking, cháy"),
                            ("02_Hydrocarbon_khong_no.md", "Alkene, Alkyne: phản ứng cộng H2, Br2, HX (quy tắc Markovnikov), trùng hợp"),
                            ("03_Arene.md", "Benzene, toluene, tính thơm (dễ thế, khó cộng, bền với tác nhân oxi hoá)")
                        ]
                    },
                    {
                        "id": "Chuong_05_Dan_xuat_halogen_alcohol_phenol",
                        "title": "Chương V: Dẫn Xuất Halogen - Alcohol - Phenol",
                        "topics": [
                            ("01_Dan_xuat_halogen.md", "Phản ứng thế nhóm -X, phản ứng tách hydro halide (quy tắc Zaitsev)"),
                            ("02_Alcohol.md", "Đặc điểm liên kết hydrogen, phản ứng với Na, phản ứng tách nước tạo alkene/ether, oxi hoá bậc 1/2"),
                            ("03_Phenol.md", "Ảnh hưởng qua lại giữa vòng benzene và nhóm -OH, phản ứng với NaOH, phản ứng thế brom vào vòng")
                        ]
                    },
                    {
                        "id": "Chuong_06_Hop_chat_carbonyl_carboxylic_acid",
                        "title": "Chương VI: Hợp Chất Carbonyl và Carboxylic Acid",
                        "topics": [
                            ("01_Aldehyde_va_ketone.md", "Nhóm >C=O, phản ứng tráng bạc với thuốc thử Tollens, phản ứng với Cu(OH)2/NaOH, phản ứng Iodoform"),
                            ("02_Carboxylic_acid.md", "Nhóm -COOH, tính acid, phản ứng ester hoá với alcohol (xúc tác H2SO4)")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Hóa Học Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Ester_Lipid_Xa_phong",
                        "title": "Chương I: Ester - Lipid - Xà Phòng và Chất Giặt Rửa",
                        "topics": [
                            ("01_Ester.md", "Khái niệm, danh pháp, tính chất vật lí, phản ứng thuỷ phân trong môi trường acid và base"),
                            ("02_Lipid_va_chat_beo.md", "Triglyceride, axit béo no/không no, chỉ số xà phòng hoá, phản ứng hydro hoá chất béo lỏng"),
                            ("03_Xa_phong_va_chat_giat_rua.md", "Cấu tạo phân tử gồm đầu ưa nước và đuôi kị nước, cơ chế làm sạch")
                        ]
                    },
                    {
                        "id": "Chuong_02_Carbohydrate",
                        "title": "Chương II: Carbohydrate",
                        "topics": [
                            ("01_Glucose_va_fructose.md", "Cấu tạo dạng mạch hở/mạch vòng, tính chất của polyalcohol và aldehyde"),
                            ("02_Saccharose_va_maltose.md", "Cấu tạo disaccharide, phản ứng thuỷ phân, phản ứng với Cu(OH)2"),
                            ("03_Tinh_bot_va_cellulose.md", "Amylose, Amylopectin, cấu trúc sợi cellulose, phản ứng màu với iot, phản ứng thuỷ phân và tạo tơ")
                        ]
                    },
                    {
                        "id": "Chuong_03_Hop_chat_chua_nitrogen",
                        "title": "Chương III: Hợp Chất Chứa Nitrogen (Amine - Amino Acid - Protein)",
                        "topics": [
                            ("01_Amine.md", "Bậc của amine, tính base so sánh giữa amine béo và aniline, phản ứng tạo phức"),
                            ("02_Amino_acid.md", "Cấu trúc lưỡng cực, tính lưỡng tính, điểm đẳng điện pI"),
                            ("03_Peptide_va_protein.md", "Liên kết peptide -CO-NH-, phản ứng thuỷ phân, phản ứng màu biuret"),
                            ("04_Enzyme_va_axit_nucleic.md", "Vai trò xúc tác sinh học của enzyme, sơ lược ADN và ARN")
                        ]
                    },
                    {
                        "id": "Chuong_04_Polymer",
                        "title": "Chương IV: Polymer và Vật Liệu Polymer",
                        "topics": [
                            ("01_Dai_cuong_ve_polymer.md", "Khái niệm monomer, mắt xích, phản ứng trùng hợp, phản ứng trùng ngưng"),
                            ("02_Vat_lieu_polymer.md", "Chất dẻo (PE, PP, PVC, PS, PMMA), tơ (nylon-6,6, capron, nitron), cao su (buna, buna-S, buna-N), keo dán")
                        ]
                    },
                    {
                        "id": "Chuong_05_Pin_dien_va_dien_phan",
                        "title": "Chương V: Pin Điện và Điện Phân",
                        "topics": [
                            ("01_The_dien_cuc_chuan.md", "Dãy thế điện cực chuẩn E^0, chiều tự diễn biến của phản ứng oxi hoá - khử"),
                            ("02_Nguon_dien_hoa_hoc.md", "Pin Galvanic (Daniell), acquy chì, pin nhiên liệu"),
                            ("03_Dien_phan.md", "Điện phân nóng chảy, điện phân dung dịch có màng ngăn, định luật Faraday")
                        ]
                    },
                    {
                        "id": "Chuong_06_Dai_cuong_kim_loai",
                        "title": "Chương VI: Đại Cương Về Kim Loại",
                        "topics": [
                            ("01_Cau_tao_va_tinh_chat_vat_ly.md", "Mạng tinh thể kim loại, electron tự do, tính dẫn điện, dẫn nhiệt, ánh kim, dẻo"),
                            ("02_Tinh_chat_hoa_hoc_va_an_mon.md", "Tính khử của kim loại, ăn mòn hoá học và ăn mòn điện hoá, các phương pháp bảo vệ kim loại"),
                            ("03_Dieu_che_kim_loai.md", "Phương pháp nhiệt luyện, thuỷ luyện, điện phân")
                        ]
                    },
                    {
                        "id": "Chuong_07_Kim_loai_nhom_A_va_phuc_chat",
                        "title": "Chương VII: Kim Loại Nhóm IA, IIA và Phức Chất",
                        "topics": [
                            ("01_Kim_loai_kiem_va_kiem_tho.md", "Tính chất kim loại kiềm (Na, K), kiềm thổ (Ca, Ba), nước cứng và cách làm mềm"),
                            ("02_So_luoc_ve_phuc_chat.md", "Nguyên tử trung tâm, phối tử, số phối trí, danh pháp và ứng dụng phức chất")
                        ]
                    }
                ]
            }
        }
    },
    "Sinh_Hoc": {
        "name": "Sinh Học",
        "icon": "🧬",
        "description": "Kiến thức Sinh học THPT: Sinh học tế bào, Vi sinh vật, Sinh học cơ thể, Di truyền học, Tiến hóa và Sinh thái học",
        "grades": {
            "Lop_10": {
                "name": "Sinh Học Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Gioi_thieu_sinh_hoc_va_cac_cap_do_to_chuc",
                        "title": "Chương I: Giới Thiệu Sinh Học và Các Cấp Độ Tổ Chức Sống",
                        "topics": [
                            ("01_Cac_cap_do_to_chuc_song.md", "Đặc tính chung của thế giới sống, các cấp độ từ phân tử đến sinh quyển")
                        ]
                    },
                    {
                        "id": "Chuong_02_Sinh_hoc_te_bao",
                        "title": "Chương II: Sinh Học Tế Bào",
                        "topics": [
                            ("01_Thanh_phan_hoa_hoc_te_bao.md", "Nước, carbohydrate, lipid, protein, nucleic acid (ADN, ARN)"),
                            ("02_Cau_truc_te_bao_nhan_so_va_nhan_thuc.md", "Màng sinh chất, nhân tế bào, ribosome, ti thể, lục lạp, lưới nội chất"),
                            ("03_Trao_doi_chat_va_chuyen_hoa_nang_luong.md", "Vận chuyển thụ động, chủ động, hô hấp tế bào, quang hợp"),
                            ("04_Chu_ki_te_bao_phan_bao.md", "Kì trung gian, nguyên phân (mitosis) và giảm phân (meiosis)")
                        ]
                    },
                    {
                        "id": "Chuong_03_Vi_sinh_vat_va_virus",
                        "title": "Chương III: Vi Sinh Vật và Virus",
                        "topics": [
                            ("01_Dai_cuong_vi_sinh_vat.md", "Các kiểu dinh dưỡng, sinh trưởng của quần thể vi sinh vật"),
                            ("02_Virus_va_benh_truyen_nhiem.md", "Cấu tạo virus, chu trình nhân lên, miễn dịch và vaccine")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Sinh Học Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Trao_doi_chat_o_thuc_vat",
                        "title": "Chương I: Trao Đổi Chất và Chuyển Hóa Năng Lượng ở Sinh Vật",
                        "topics": [
                            ("01_Trao_doi_nuoc_va_khoang_o_thuc_vat.md", "Hấp thụ nước và ion khoáng, dòng mạch gỗ và mạch rây, thoát hơi nước qua khí khổng"),
                            ("02_Quang_hop_va_ho_hap_o_thuc_vat.md", "Quang hợp ở nhóm thực vật C3, C4, CAM; hô hấp sáng"),
                            ("03_Tieu_hoa_ho_hap_o_dong_vat.md", "Ống tiêu hóa, bề mặt trao đổi khí ở động vật (da, mang, hệ thống ống khí, phổi)"),
                            ("04_Tuan_hoan_va_bai_tiet.md", "Hệ tuần hoàn hở và kín, huyết áp, cơ chế điều hòa cân bằng nội môi qua thận")
                        ]
                    },
                    {
                        "id": "Chuong_02_Cam_ung_o_sinh_vat",
                        "title": "Chương II: Cảm Ứng ở Sinh Vật",
                        "topics": [
                            ("01_Cam_ung_o_thuc_vat.md", "Hướng động và ứng động ở thực vật"),
                            ("02_Cam_ung_o_dong_vat.md", "Hệ thần kinh dạng lưới, chuỗi hạch, dạng ống; phản xạ không điều kiện và có điều kiện")
                        ]
                    },
                    {
                        "id": "Chuong_03_Sinh_truong_va_sinh_san",
                        "title": "Chương III: Sinh Trưởng, Phát Triển và Sinh Sản ở Sinh Vật",
                        "topics": [
                            ("01_Sinh_truong_va_phat_trien.md", "Mô phân sinh, hoocmôn thực vật (auxin, gibberellin, cytokinine...), phát triển qua biến thái ở động vật"),
                            ("02_Sinh_san_vo_tinh_va_huu_tinh.md", "Sinh sản vô tính, thụ phấn và thụ tinh kép ở thực vật, sinh sản hữu tính ở động vật")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Sinh Học Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Di_truyen_phan_tu",
                        "title": "Chương I: Di Truyền Phân Tử",
                        "topics": [
                            ("01_Gen_ma_di_truyen_tai_ban_ADN.md", "Cấu trúc ADN, mã di truyền, cơ chế tái bản ADN bán bảo toàn"),
                            ("02_Phien_ma_va_dich_ma.md", "Quá trình tổng hợp ARN (phiên mã), tổng hợp chuỗi polypeptide (dịch mã)"),
                            ("03_Dieu_hoa_hoat_dong_cua_gen.md", "Mô hình Operon Lac ở vi khuẩn E. coli"),
                            ("04_Dot_bien_gen.md", "Đột biến điểm: thay thế, thêm, mất cặp nucleotide và hậu quả")
                        ]
                    },
                    {
                        "id": "Chuong_02_Di_truyen_nhiem_sac_the",
                        "title": "Chương II: Di Truyền Nhiễm Sắc Thể",
                        "topics": [
                            ("01_Nhiem_sac_the_va_dot_bien_NST.md", "Cấu trúc NST, đột biến cấu trúc (mất, lặp, đảo, chuyển đoạn), đột biến số lượng (lệch bội, đa bội)"),
                            ("02_Quy_luat_di_truyen_Mendel.md", "Quy luật phân li, quy luật phân li độc lập, tương tác gen"),
                            ("03_Lien_ket_gen_va_hoan_vi_gen.md", "Quy luật liên kết hoàn toàn của Morgan, hoán vị gen và khoảng cách bản đồ di truyền"),
                            ("04_Di_truyen_lien_ket_gioi_tinh.md", "Di truyền chéo trên NST X, di truyền thẳng trên NST Y, di truyền ngoài nhân")
                        ]
                    },
                    {
                        "id": "Chuong_03_Di_truyen_quan_the",
                        "title": "Chương III: Di Truyền Quần Thể",
                        "topics": [
                            ("01_Cau_truc_di_truyen_quan_the.md", "Quần thể tự phối, quần thể ngẫu phối, định luật Hardy - Weinberg: p^2 + 2pq + q^2 = 1")
                        ]
                    },
                    {
                        "id": "Chuong_04_Tien_hoa",
                        "title": "Chương IV: Tiến Hóa",
                        "topics": [
                            ("01_Hoc_thuyet_tien_hoa_tong_hop_hien_dai.md", "Các nhân tố tiến hoá: Đột biến, Di - nhập gen, Chọn lọc tự nhiên, Phiêu bạt di truyền, Giao phối không ngẫu nhiên"),
                            ("02_Su_hinh_thanh_loai_moi.md", "Cách li địa lí, cách li sinh thái, cách li tập tính, con đường lai xa và đa bội hoá")
                        ]
                    },
                    {
                        "id": "Chuong_05_Sinh_thai_hoc",
                        "title": "Chương V: Sinh Thái Học và Môi Trường",
                        "topics": [
                            ("01_Sinh_thai_hoc_ca_the_va_quan_the.md", "Nhân tố sinh thái, giới hạn sinh thái, đặc trưng quần thể (kích thước, mật độ, tỉ lệ giới tính)"),
                            ("02_Quan_xa_sinh_vat.md", "Cấu trúc quần xã, diễn thế sinh thái nguyên sinh và thứ sinh, quan hệ cộng sinh/kí sinh/cạnh tranh"),
                            ("03_He_sinh_thai_va_chu_trinh_sinh_dia_hoa.md", "Chuỗi và lưới thức ăn, tháp sinh thái, chu trình carbon, nito, bảo vệ đa dạng sinh học")
                        ]
                    }
                ]
            }
        }
    },
    "Tin_Hoc": {
        "name": "Tin Học",
        "icon": "💻",
        "description": "Tin học phổ thông & Định hướng Khoa học máy tính: Python, Thuật toán, Cơ sở dữ liệu (SQL), Mạng máy tính, An toàn thông tin và AI",
        "grades": {
            "Lop_10": {
                "name": "Tin Học Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_May_tinh_va_xa_hoi_tri_thuc",
                        "title": "Chương I: Máy Tính và Xã Hội Tri Thức",
                        "topics": [
                            ("01_Du_lieu_va_thong_tin.md", "Biểu diễn dữ liệu số, văn bản, hình ảnh, âm thanh trong máy tính"),
                            ("02_Kien_truc_may_tinh_va_he_dieu_hanh.md", "Phần cứng, kiến trúc Von Neumann, chức năng của hệ điều hành")
                        ]
                    },
                    {
                        "id": "Chuong_02_Lap_trinh_Python_co_ban",
                        "title": "Chương II: Lập Trình Cơ Bản Với Python",
                        "topics": [
                            ("01_Bien_kieu_du_lieu_toan_tu.md", "Biến, kiểu dữ liệu int, float, str, bool, các toán tử số học và logic"),
                            ("02_Cau_truc_re_nhanh.md", "Cấu trúc if, if-else, if-elif-else trong Python"),
                            ("03_Cau_truc_lap.md", "Vòng lặp for với range(), vòng lặp while, lệnh break và continue"),
                            ("04_Ham_va_chuong_trinh_con.md", "Khai báo hàm def, tham số, giá trị trả về return, phạm vi biến")
                        ]
                    },
                    {
                        "id": "Chuong_03_Cau_truc_du_lieu_danh_sach",
                        "title": "Chương III: Cấu Trúc Dữ Liệu Danh Sách (List) và Xâu Kí Tự (String)",
                        "topics": [
                            ("01_Xau_ki_tu_string.md", "Các thao tác với xâu, cắt lát string slice, hàm len, split, join, strip"),
                            ("02_Danh_sach_list.md", "Khởi tạo list, thêm phần tử append, xoá remove, duyệt danh sách"),
                            ("03_Thuat_toan_tim_kiem_va_sap_xep_co_ban.md", "Tìm kiếm tuần tự, tìm kiếm nhị phân, sắp xếp nổi bọt (Bubble Sort), sắp xếp chọn (Selection Sort)")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Tin Học Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_He_quan_tri_co_so_du_lieu",
                        "title": "Chương I: Cơ Sở Dữ Liệu và Hệ Quản Trị CSDL",
                        "topics": [
                            ("01_Khai_niem_co_so_du_lieu.md", "Khái niệm CSDL, mô hình quan hệ, bảng, bản ghi, trường, khoá chính, khoá ngoại"),
                            ("02_Ngon_ngu_truy_van_SQL.md", "Các lệnh cơ bản: SELECT, FROM, WHERE, GROUP BY, ORDER BY, JOIN")
                        ]
                    },
                    {
                        "id": "Chuong_02_Thuat_toan_nang_cao",
                        "title": "Chương II: Thuật Toán và Kĩ Thuật Lập Trình",
                        "topics": [
                            ("01_Kieu_du_lieu_dictionary_va_set.md", "Cấu trúc từ điển Dict {key: value} và tập hợp Set trong Python"),
                            ("02_De_quy_va_chia_de_tri.md", "Tư duy đệ quy, bài toán tháp Hà Nội, thuật toán sắp xếp nhanh QuickSort, MergeSort")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Tin Học Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Mang_may_tinh_va_internet",
                        "title": "Chương I: Mạng Máy Tính và Internet",
                        "topics": [
                            ("01_Mo_hinh_mang_va_giao_thuc.md", "Mô hình TCP/IP, địa chỉ IP (IPv4, IPv6), giao thức HTTP/HTTPS, DNS"),
                            ("02_An_toan_thong_tin_mang.md", "Mã hoá dữ liệu, tường lửa, phòng chống mã độc, tấn công mạng")
                        ]
                    },
                    {
                        "id": "Chuong_02_Tri_tue_nhan_tao_va_cong_nghe_moi",
                        "title": "Chương II: Trí Tuệ Nhân Tạo (AI) và Công Nghệ Mới",
                        "topics": [
                            ("01_Tong_quan_ve_tri_tue_nhan_tao.md", "Khái niệm AI, Machine Learning (học máy), Deep Learning (học sâu)"),
                            ("02_Ung_dung_va_dao_duc_AI.md", "Xử lí ngôn ngữ tự nhiên, thị giác máy tính, đạo đức và tác động xã hội của AI")
                        ]
                    }
                ]
            }
        }
    },
    "Ngu_Van": {
        "name": "Ngữ Văn",
        "icon": "📚",
        "description": "Hệ thống văn học Việt Nam và thế giới, Tiếng Việt, Kĩ năng viết bài nghị luận văn học và nghị luận xã hội",
        "grades": {
            "Lop_10": {
                "name": "Ngữ Văn Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Than_thoai_va_su_thi",
                        "title": "Chương I: Thần Thoại và Sử Thi",
                        "topics": [
                            ("01_Dac_trung_than_thoai_su_thi.md", "Không gian, thời gian kì ảo, người anh hùng sử thi Đăm Săn, Ô-đi-xê")
                        ]
                    },
                    {
                        "id": "Chuong_02_Tho_tru_tinh_va_nghe_thuat_tu_tuong",
                        "title": "Chương II: Thơ Trữ Tình Trung Đại và Hiện Đại",
                        "topics": [
                            ("01_Tho_duong_luat_va_tho_luc_bat.md", "Quy luật gieo vần, niêm luật, bút pháp ước lệ tượng trưng")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Ngữ Văn Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Truyen_ngan_va_tieu_thuyet_hien_dai",
                        "title": "Chương I: Truyện Ngắn và Tiểu Thuyết Hiện Đại",
                        "topics": [
                            ("01_Nghe_thuat_xay_dung_nhan_vat_va_tinh_huong.md", "Điểm nhìn trần thuật, tình huống truyện, phân tích tâm lí nhân vật")
                        ]
                    },
                    {
                        "id": "Chuong_02_Tho_moi_va_bien_chuyen_nghe_thuat",
                        "title": "Chương II: Phong Trào Thơ Mới (1932 - 1945)",
                        "topics": [
                            ("01_Cai_toi_ca_nhan_trong_tho_moi.md", "Xuân Diệu, Huy Cận, Hàn Mặc Tử - Cuộc cách mạng trong thi ca Việt Nam")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Ngữ Văn Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Van_hoc_Viet_Nam_1945_den_het_the_ki_XX",
                        "title": "Chương I: Văn Học Việt Nam Từ 1945 Đến Hết Thế Kỉ XX",
                        "topics": [
                            ("01_Khai_quat_van_hoc_1945_1975.md", "Khuynh hướng sử thi và cảm hứng lãng mạn"),
                            ("02_Van_hoc_thoi_ki_doi_moi_sau_1975.md", "Cảm hứng thế sự, đời tư, tinh thần nhân bản và đổi mới thi pháp")
                        ]
                    },
                    {
                        "id": "Chuong_02_Ki_nang_nghi_luan_xa_hoi_va_van_hoc",
                        "title": "Chương II: Kĩ Năng Viết Bài Nghị Luận Chuyên Sâu",
                        "topics": [
                            ("01_Nghi_luan_ve_mot_tu_tuong_dao_ly.md", "Cấu trúc bài viết 4 bước: Giải thích, bàn luận chứng minh, mở rộng phản đề, bài học"),
                            ("02_Nghi_luan_ve_mot_hien_tuong_doi_song.md", "Thực trạng, nguyên nhân, hậu quả/tác dụng, giải pháp và liên hệ bản thân"),
                            ("03_Nghi_luan_van_hoc_so_sanh_danh_gia.md", "So sánh hai đoạn thơ, hai hình tượng nhân vật, đánh giá ý kiến bàn về văn học")
                        ]
                    }
                ]
            }
        }
    },
    "Tieng_Anh": {
        "name": "Tiếng Anh",
        "icon": "🌐",
        "description": "Ngữ pháp tiếng Anh THPT toàn diện: Thì động từ, Câu bị động, Câu điều kiện, Mệnh đề quan hệ, Đảo ngữ, Từ vựng theo chủ đề",
        "grades": {
            "Lop_10": {
                "name": "Tiếng Anh Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Tenses_and_Verb_Forms",
                        "title": "Chapter I: Tenses and Verb Forms",
                        "topics": [
                            ("01_Present_and_Past_Tenses.md", "Present Simple, Present Continuous, Present Perfect, Past Simple, Past Continuous"),
                            ("02_Gerund_and_Infinitive.md", "V-ing vs. To-V, động từ theo sau bởi cả V-ing và To-V đổi nghĩa (remember, stop, try...)")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Tiếng Anh Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Complex_Structures",
                        "title": "Chapter I: Complex Grammatical Structures",
                        "topics": [
                            ("01_Modal_Verbs_in_Past.md", "Must have V3/ed, Should have V3/ed, Can't have V3/ed"),
                            ("02_Conditionals_and_Wishes.md", "Type 1, 2, 3, Mixed conditionals, Inversion in conditionals (Should/Were/Had)")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Tiếng Anh Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Advanced_Grammar_for_Graduation",
                        "title": "Chapter I: Advanced Grammar for High School Graduation Exam",
                        "topics": [
                            ("01_Passive_Voice_Advanced.md", "Thể bị động đặc biệt: It is said that..., causatives (have/get sth done), passive with gerunds"),
                            ("02_Relative_Clauses_and_Reduction.md", "Mệnh đề quan hệ xác định/không xác định, rút gọn bằng V-ing, V-ed, To-V"),
                            ("03_Inversion_Structures.md", "Đảo ngữ với Never, Rarely, Scarcely, Not only... but also, No sooner... than"),
                            ("04_Subjunctive_Mood_and_Collocations.md", "Câu giả định thức, cụm từ cố định (collocations), idioms và phrasal verbs trọng tâm")
                        ]
                    }
                ]
            }
        }
    },
    "Lich_Su": {
        "name": "Lịch Sử",
        "icon": "🏛️",
        "description": "Lịch sử thế giới và Lịch sử Việt Nam từ nguồn gốc đến thời kì đổi mới và hội nhập quốc tế",
        "grades": {
            "Lop_10": {
                "name": "Lịch Sử Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Lich_su_va_su_hoc",
                        "title": "Chương I: Lịch Sử và Sử Học",
                        "topics": [
                            ("01_Hien_thuc_lich_su_va_tri_thuc_lich_su.md", "Khái niệm hiện thực lịch sử, tri thức lịch sử và phương pháp nghiên cứu")
                        ]
                    },
                    {
                        "id": "Chuong_02_Cac_nen_van_minh_the_gioi_co_trung_dai",
                        "title": "Chương II: Các Nền Văn Minh Thế Giới Cổ - Trung Đại",
                        "topics": [
                            ("01_Van_minh_Ai_Cap_va_Luu_Vuc_Song_An_Song_Hang.md", "Thành tựu chữ viết, kiến trúc kim tự tháp, tôn giáo và khoa học")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Lịch Sử Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Cach_mang_tu_san_va_su_phat_trien_chu_nghia_tu_ban",
                        "title": "Chương I: Cách Mạng Tư Sản và Sự Phát Triển Của Chủ Nghĩa Tư Bản",
                        "topics": [
                            ("01_Cac_cuoc_cach_mang_tu_san_tieu_bieu.md", "Cách mạng Anh, Bắc Mĩ, Pháp - Tiền đề, động lực và ý nghĩa lịch sử")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Lịch Sử Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_The_gioi_sau_chien_tranh_the_gioi_thu_hai",
                        "title": "Chương I: Thế Giới Sau Chiến Tranh Thế Giới Thứ Hai (1945 Đến Nay)",
                        "topics": [
                            ("01_Lien_Hop_Quoc_va_trat_tu_hai_cuc_Ianta.md", "Hội nghị Ianta, thành lập Liên Hợp Quốc, cục diện Chiến tranh Lạnh"),
                            ("02_Xu_the_toan_cau_hoa_va_the_gioi_da_cuc.md", "Sự sụp đổ của trật tự hai cực, xu thế hoà hoãn, đa cực hoá kinh tế và chính trị")
                        ]
                    },
                    {
                        "id": "Chuong_02_Lich_su_Viet_Nam_1919_den_nay",
                        "title": "Chương II: Lịch Sử Việt Nam Hiện Đại (1919 Đến Nay)",
                        "topics": [
                            ("01_Phong_trao_dan_toc_dan_chu_1919_1930.md", "Khai thác thuộc địa lần 2 của Pháp, Nguyễn Ái Quốc và sự thành lập Đảng Cộng sản Việt Nam (1930)"),
                            ("02_Cach_mang_Thang_Tam_1945.md", "Khởi nghĩa từng phần, Tổng khởi nghĩa Tháng Tám năm 1945, Nước VNDCCH ra đời"),
                            ("03_Khang_chien_chong_Phap_1945_1954.md", "Chiến dịch Việt Bắc (1947), Biên Giới (1950), Điện Biên Phủ (1954), Hiệp định Genève"),
                            ("04_Khang_chien_chong_My_1954_1975.md", "Phong trào Đồng khởi, đánh bại 4 chiến lược chiến tranh của Mỹ, Đại thắng mùa Xuân 1975"),
                            ("05_Cong_cuoc_Doi_moi_tu_1986_den_nay.md", "Đường lối đổi mới của Đại hội VI (1986), thành tựu kinh tế, xã hội, đối ngoại")
                        ]
                    }
                ]
            }
        }
    },
    "Dia_Ly": {
        "name": "Địa Lí",
        "icon": "🌍",
        "description": "Địa lí tự nhiên, Địa lí kinh tế - xã hội thế giới và Địa lí Việt Nam toàn diện",
        "grades": {
            "Lop_10": {
                "name": "Địa Lí Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Su_dung_ban_do_va_GPS",
                        "title": "Chương I: Sử Dụng Bản Đồ và Hệ Thống Định Vị Toàn Cầu (GPS)",
                        "topics": [
                            ("01_Phuong_phap_bieu_hien_cac_doi_tuong_dia_ly.md", "Phương pháp kí hiệu, đường chuyển động, chấm điểm, bản đồ số và GPS")
                        ]
                    },
                    {
                        "id": "Chuong_02_Dia_ly_tu_nhien_trai_dat",
                        "title": "Chương II: Các Vỏ Địa Lí Của Trái Đất",
                        "topics": [
                            ("01_Thach_quyen_va_noi_ngoai_luc.md", "Cấu tạo thạch quyển, mảng kiến tạo, tác động của nội lực và ngoại lực"),
                            ("02_Khi_quyen_khi_hau_gio.md", "Sự phân bố nhiệt độ không khí, khí áp, các loại gió chính trên Trái Đất")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "Địa Lí Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Dia_ly_kinh_te_xa_hoi_the_gioi",
                        "title": "Chương I: Địa Lí Khu Vực và Các Nền Kinh Tế Lớn",
                        "topics": [
                            ("01_Hop_chung_quoc_Hoa_Ky_USA.md", "Vị trí địa lí, tài nguyên thiên nhiên, đặc điểm kinh tế và các vùng kinh tế Hoa Kỳ"),
                            ("02_Lien_minh_Chau_Au_EU.md", "Quá trình hình thành, vị thế kinh tế, thị trường chung châu Âu"),
                            ("03_Khu_vuc_Dong_Nam_A_ASEAN.md", "Vị trí chiến lược, tự nhiên, dân cư, mục tiêu và thành tựu của ASEAN")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "Địa Lí Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Dia_ly_tu_nhien_Viet_Nam",
                        "title": "Chương I: Địa Lí Tự Nhiên Việt Nam",
                        "topics": [
                            ("01_Vi_tri_dia_ly_va_pham_vi_lanh_tho.md", "Toạ độ địa lí, ý nghĩa vị trí địa lí đối với tự nhiên, kinh tế, quốc phòng"),
                            ("02_Dac_diem_chung_cua_tu_nhien_Viet_Nam.md", "Đất nước nhiều đồi núi, tính chất nhiệt đới ẩm gió mùa, thiên nhiên phân hoá đa dạng")
                        ]
                    },
                    {
                        "id": "Chuong_02_Dia_ly_dan_cu_va_kinh_te_Viet_Nam",
                        "title": "Chương II: Địa Lí Dân Cư và Các Ngành Kinh Tế",
                        "topics": [
                            ("01_Dia_ly_dan_cu_va_nguon_lao_dong.md", "Quy mô, cơ cấu dân số, phân bố dân cư, đô thị hoá và chuyển dịch lao động"),
                            ("02_Chuyen_dich_co_cau_kinh_te.md", "Chuyển dịch cơ cấu ngành kinh tế, thành phần kinh tế và lãnh thổ"),
                            ("03_Dia_ly_cac_nganh_kinh_te_trong_tam.md", "Nông nghiệp (trồng trọt, chăn nuôi), Công nghiệp (năng lượng, chế biến), Dịch vụ (giao thông, du lịch)")
                        ]
                    },
                    {
                        "id": "Chuong_03_Dia_ly_cac_vung_kinh_te_trong_diem",
                        "title": "Chương III: Địa Lí Các Vùng Kinh Tế",
                        "topics": [
                            ("01_Trung_du_va_mien_nui_Bac_Bo.md", "Thế mạnh khai thác khoáng sản, thuỷ điện, cây công nghiệp cận nhiệt và ôn đới"),
                            ("02_Dong_bang_song_Hong.md", "Thế mạnh nông nghiệp thâm canh, cơ sở hạ tầng, vấn đề việc làm và chuyển dịch cơ cấu"),
                            ("03_Bac_Trung_Bo_va_Duyen_hai_Nam_Trung_Bo.md", "Phát triển kinh tế biển, rừng, du lịch và giải quyết thiên tai"),
                            ("04_Tay_Nguyen.md", "Phát triển cây công nghiệp lâu năm (cà phê, cao su, hồ tiêu), thuỷ năng"),
                            ("05_Dong_Nam_Bo.md", "Vùng kinh tế dẫn đầu cả nước, phát triển công nghiệp và dịch vụ hiện đại"),
                            ("06_Dong_bang_song_Cuu_Long.md", "Vựa lúa, thuỷ sản lớn nhất, thích ứng với biến đổi khí hậu và xâm nhập mặn"),
                            ("07_Kinh_te_bien_dao_va_an_ninh_chu_quyen.md", "Vùng biển đặc quyền kinh tế, quần đảo Hoàng Sa, Trường Sa, khai thác tổng hợp kinh tế biển")
                        ]
                    }
                ]
            }
        }
    },
    "GDKT_va_PL": {
        "name": "Giáo Dục Kinh Tế và Pháp Luật",
        "icon": "⚖️",
        "description": "Kiến thức Kinh tế học cơ bản, Thị trường, Tài chính và Hệ thống Pháp luật Việt Nam",
        "grades": {
            "Lop_10": {
                "name": "GDKT & PL Lớp 10",
                "chapters": [
                    {
                        "id": "Chuong_01_Kinh_te_hoc_co_ban",
                        "title": "Chương I: Nền Kinh Tế và Các Hoạt Động Kinh Tế",
                        "topics": [
                            ("01_Cac_hoat_dong_kinh_te_co_ban.md", "Sản xuất, phân phối, trao đổi, tiêu dùng và các chủ thể trong nền kinh tế"),
                            ("02_Thi_truong_va_co_che_thi_truong.md", "Quy luật cung - cầu, quy luật giá trị, chức năng của thị trường")
                        ]
                    }
                ]
            },
            "Lop_11": {
                "name": "GDKT & PL Lớp 11",
                "chapters": [
                    {
                        "id": "Chuong_01_Thi_truong_tai_chinh_va_doanh_nghiep",
                        "title": "Chương I: Thị Trường Tài Chính và Doanh Nghiệp",
                        "topics": [
                            ("01_Lam_phat_va_that_nghiep.md", "Khái niệm lạm phát, nguyên nhân, hậu quả và các biện pháp kiểm soát"),
                            ("02_Thi_truong_lao_dong_va_viec_lam.md", "Cung cầu lao động, xu hướng thị trường lao động trong kỉ nguyên số")
                        ]
                    }
                ]
            },
            "Lop_12": {
                "name": "GDKT & PL Lớp 12",
                "chapters": [
                    {
                        "id": "Chuong_01_Tang_truong_va_phat_trien_kinh_te",
                        "title": "Chương I: Tăng Trưởng và Phát Triển Kinh Tế",
                        "topics": [
                            ("01_Tang_truong_kinh_te_GDP_GNI.md", "Chỉ số GDP, GNI, HDI và phát triển kinh tế bền vững"),
                            ("02_Hoi_nhap_kinh_te_quoc_te.md", "Toàn cầu hoá, các hiệp định thương mại tự do FTA, cơ hội và thách thức")
                        ]
                    },
                    {
                        "id": "Chuong_02_He_thong_phap_luat_va_quyen_cong_dan",
                        "title": "Chương II: Quyền và Nghĩa Vụ Cơ Bản Của Công Dân",
                        "topics": [
                            ("01_Quyen_binh_dang_cua_cong_dan.md", "Bình đẳng trước pháp luật, bình đẳng về quyền và nghĩa vụ"),
                            ("02_Quyen_tu_do_co_ban_cua_cong_dan.md", "Bất khả xâm phạm về thân thể, tự do ngôn luận, quyền bầu cử và ứng cử"),
                            ("03_Phap_luat_ve_kinh_doanh_va_thue.md", "Quyền tự do kinh doanh, nghĩa vụ nộp thuế, bảo vệ quyền lợi người tiêu dùng")
                        ]
                    }
                ]
            }
        }
    }
}

def create_directory_structure(base_dir="."):
    print(f"Scaffolding curriculum inside '{base_dir}'...")
    total_dirs = 0
    total_files = 0

    for subject_key, subject_data in CURRICULUM_DATA.items():
        subject_dir = os.path.join(base_dir, subject_key)
        os.makedirs(subject_dir, exist_ok=True)
        total_dirs += 1

        # Subject README
        subj_readme_path = os.path.join(subject_dir, "README.md")
        with open(subj_readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {subject_data['icon']} Môn: {subject_data['name']}\n\n")
            f.write(f"> {subject_data['description']}\n\n")
            f.write("## 📚 Danh Mục Lớp Học\n\n")
            for grade_key, grade_data in subject_data["grades"].items():
                f.write(f"- 🎓 [**{grade_data['name']}**](./{grade_key}/README.md)\n")
                for ch in grade_data["chapters"]:
                    f.write(f"  - 📖 [{ch['title']}](./{grade_key}/{ch['id']}/README.md) ({len(ch['topics'])} chủ đề)\n")
            f.write("\n---\n*Kho kiến thức THPT - GDPT 2018*\n")
        total_files += 1

        for grade_key, grade_data in subject_data["grades"].items():
            grade_dir = os.path.join(subject_dir, grade_key)
            os.makedirs(grade_dir, exist_ok=True)
            total_dirs += 1

            # Grade README
            grade_readme_path = os.path.join(grade_dir, "README.md")
            with open(grade_readme_path, "w", encoding="utf-8") as f:
                f.write(f"# 🎓 {grade_data['name']} - {subject_data['name']}\n\n")
                f.write(f"[⬅ Quay lại danh mục {subject_data['name']}](../README.md)\n\n")
                f.write("## 📑 Danh Sách Các Chương\n\n")
                for idx, ch in enumerate(grade_data["chapters"], 1):
                    f.write(f"### {ch['title']}\n")
                    f.write(f"- 📁 Đường dẫn: [`{ch['id']}`](./{ch['id']}/README.md)\n")
                    f.write(f"- 📝 Danh sách bài học ({len(ch['topics'])} bài):\n")
                    for top_file, top_name in ch["topics"]:
                        f.write(f"  - 📄 [{top_name}](./{ch['id']}/{top_file})\n")
                    f.write("\n")
                f.write("---\n*Hệ thống kiến thức chuẩn GDPT 2018*\n")
            total_files += 1

            for ch in grade_data["chapters"]:
                ch_dir = os.path.join(grade_dir, ch["id"])
                os.makedirs(ch_dir, exist_ok=True)
                total_dirs += 1

                # Chapter README
                ch_readme_path = os.path.join(ch_dir, "README.md")
                with open(ch_readme_path, "w", encoding="utf-8") as f:
                    f.write(f"# 📖 {ch['title']}\n\n")
                    f.write(f"**Môn học:** [{subject_data['name']}](../../README.md) | **Cấp độ:** [{grade_data['name']}](../README.md)\n\n")
                    f.write("## 🎯 Mục Tiêu Chương\n")
                    f.write("- Nắm vững hệ thống định nghĩa, tính chất, định lý cốt lõi.\n")
                    f.write("- Vận dụng thành thạo các công thức toán - lí - hoá vào giải bài tập trắc nghiệm và tự luận.\n")
                    f.write("- Rèn luyện kĩ năng đọc hiểu sơ đồ, đồ thị và bảng số liệu.\n\n")
                    f.write("## 📑 Danh Sách Các Chủ Đề\n\n")
                    for top_file, top_name in ch["topics"]:
                        f.write(f"- 📄 [**{top_name}**](./{top_file})\n")
                    f.write("\n---\n[⬅ Quay lại mục lục Lớp](../README.md) | [🏠 Trang chủ repo](../../../README.md)\n")
                total_files += 1

                for top_file, top_name in ch["topics"]:
                    top_path = os.path.join(ch_dir, top_file)
                    # We will create standard placeholder if not customized
                    if not os.path.exists(top_path):
                        with open(top_path, "w", encoding="utf-8") as f:
                            f.write(f"# 📌 {top_name}\n\n")
                            f.write(f"> **Môn học:** {subject_data['name']} | **Lớp:** {grade_data['name']} | **Chương:** {ch['title']}\n\n")
                            f.write("## 🎯 Mục Tiêu Bài Học\n")
                            f.write(f"- Hiểu rõ bản chất kiến thức: **{top_name}**.\n")
                            f.write("- Ghi nhớ hệ thống công thức then chốt và phương pháp giải nhanh.\n")
                            f.write("- Vận dụng giải các bài toán từ mức độ nhận biết, thông hiểu đến vận dụng cao.\n\n")
                            f.write("## 📖 I. Lý Thuyết Trọng Tâm\n\n")
                            f.write("*(Nội dung lí thuyết trọng tâm đang được hoàn thiện chi tiết theo chương trình GDPT 2018...)*\n\n")
                            f.write("## 🔢 II. Hệ Thống Công Thức Cần Nhớ\n\n")
                            f.write("```math\n\\text{Đang cập nhật công thức LaTeX}\n```\n\n")
                            f.write("## 📊 III. Sơ Đồ Tư Duy & Hình Biểu Diễn\n\n")
                            f.write("```mermaid\ngraph TD\n    A[" + top_name + "] --> B[Định Nghĩa]\n    A --> C[Công Thức]\n    A --> D[Dạng Bài Tập]\n```\n\n")
                            f.write("## 💡 IV. Các Dạng Bài Tập & Phương Pháp Giải\n\n")
                            f.write("### Dạng 1: Nhận biết và thông hiểu kiến thức cơ bản\n")
                            f.write("- **Phương pháp:** Sử dụng trực tiếp định nghĩa và công thức cơ bản.\n\n")
                            f.write("## 📝 V. Ví Dụ Minh Họa Có Lời Giải\n\n")
                            f.write("*(Ví dụ minh họa và bài tập trắc nghiệm đang được cập nhật...)*\n\n")
                            f.write("---\n[⬅ Quay lại danh mục chương](./README.md)\n")
                        total_files += 1

    print(f"Created {total_dirs} directories and {total_files} files successfully!")

if __name__ == "__main__":
    create_directory_structure(".")
