# BÀI TẬP LỚN: Hệ thống quản lý sinh viên trường đại học Thăng Long

## Tóm tắt dự án
Dự án "Hệ thống Quản lý Điểm Sinh Viên" là một phần mềm Desktop được phát triển bằng Python kết hợp với nền tảng Microsoft Power BI. Mục tiêu của dự án là số hóa và tự động hóa toàn bộ quy trình quản lý điểm số: từ khâu đọc và làm sạch dữ liệu thô (CSV), chuẩn hóa thông tin, đến phân tích thống kê và trực quan hóa. Hệ thống giúp người dùng dễ dàng theo dõi, thao tác với dữ liệu, đồng thời cung cấp cái nhìn trực quan, đa chiều về tình hình và chất lượng học tập của sinh viên.

## Nhóm nghiên cứu
- **Đơn vị:** Trường Đại học Thăng Long
- **Giảng viên hướng dẫn:** ThS. Nguyễn Hùng Cường

- **Thành viên:**
- A49828 Nguyễn Hồng Sơn
- A49971 Lê Nguyễn Nhật Huy
- A56677 Lê Quang Khải
- A51575 Huỳnh Hải Nam

---

## Phương pháp thực hiện

Dự án được triển khai theo quy trình xử lý dữ liệu tiêu chuẩn kết hợp với phát triển phần mềm module hóa:

1. **Thu thập và Chuẩn bị dữ liệu (Data Preparation):** 
   * Dữ liệu điểm số sinh viên được tập hợp và lưu trữ ban đầu dưới dạng file `raw_tlu.csv`.
2. **Làm sạch và Xử lý dữ liệu (Data Cleaning & Processing):** 
   * Sử dụng thư viện **Pandas** để đọc và nạp dữ liệu.
   * Chuẩn hóa tên cột, loại bỏ các dòng thiếu dữ liệu (`NaN`) hoặc có điểm số không hợp lệ (nhỏ hơn 0 hoặc lớn hơn 10).
   * Áp dụng các hàm logic tự động tính toán "Xếp loại" (Dựa trên thang điểm: >= 8.5 là A, >= 7.0 là B...) và "Kết quả" (Đạt/Học lại) dựa trên điểm số thực tế.
   * Lưu trữ dữ liệu đã xử lý ra định dạng `cleaned_tlu.csv`.
3. **Quản lý Trạng thái và Nghiệp vụ (State Management):**
   * Xây dựng module `state` (`AppState`) độc lập để theo dõi và cập nhật trạng thái dữ liệu (bộ lọc tìm kiếm, dữ liệu toàn cục) liên tục giữa các tác vụ người dùng.
4. **Thiết kế Giao diện (UI/UX Design):**
   * Sử dụng **Tkinter** thiết kế giao diện Desktop, chia layout theo các Frame: Form tìm kiếm, Form Admin quản trị, Bảng Treeview hiển thị dữ liệu và Khu vực gọi biểu đồ.
5. **Trực quan hóa dữ liệu (Data Visualization):**
   * **Tích hợp Python:** Viết các hàm sử dụng **Matplotlib** để vẽ biểu đồ tại chỗ theo dữ liệu đã lọc.

---

## Kết quả bài tập lớn
1. **Ứng dụng Desktop hoàn chỉnh:** Xây dựng thành công phần mềm với giao diện đồ họa (GUI) dễ sử dụng bằng Tkinter, hoạt động ổn định và có khả năng điều hướng mượt mà.
2. **Quy trình Xử lý dữ liệu chuẩn hóa:** Tự động hóa việc loại bỏ dữ liệu lỗi, quy đổi điểm số sang điểm chữ (A, B, C, D, F) và đánh giá trạng thái (Đạt/Học lại) thông qua thư viện Pandas, xuất ra file dữ liệu sạch (`cleaned_tlu.csv`).
3. **Hệ thống Biểu đồ Tích hợp:** Triển khai thành công 5 loại biểu đồ phân tích thống kê trực tiếp trên giao diện ứng dụng (Phân bố điểm, Tương quan tín chỉ, Trung bình kỳ học, Tỷ lệ xếp loại, Xu hướng học tập) nhờ Matplotlib.

--- 

  ### 1. Quản lý Dữ liệu (BackEnd)
* **Tự động hóa dữ liệu:** Đọc, làm sạch và chuẩn hóa dữ liệu từ file CSV. Hệ thống tự động tạo file mẫu nếu không tìm thấy dữ liệu gốc.
* **Lọc và tìm kiếm:** Tìm kiếm nhanh theo Tên môn, Mã sinh viên hoặc Mã học phần.
* **Quản trị (Admin):** Hỗ trợ Thêm, Sửa, Xóa thông tin sinh viên trực tiếp trên giao diện.
* **State Manager:** Đồng bộ hóa trạng thái dữ liệu (bộ lọc, dữ liệu đang hiển thị) trên toàn bộ hệ thống.

  ### 2. Giao diện & Trực quan hóa (FrontEnd)
* **Giao diện Desktop:** Xây dựng bằng Tkinter, hiển thị dữ liệu trực quan bằng bảng (Treeview).
* **Biểu đồ tích hợp:** Tích hợp Matplotlib để vẽ biểu đồ tương tác ngay trên ứng dụng (Histogram, Scatter, Bar, Pie, Line).
* **Kết nối Power BI:** Hỗ trợ xuất dữ liệu đã làm sạch (`cleaned_tlu.csv`) để trực quan hóa nâng cao trên Power BI Dashboard.


---

  ### 3. Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.12 
* **Thư viện UI:** Tkinter 
* **Xử lý dữ liệu:** Pandas 
* **Vẽ biểu đồ:** Matplotlib 
* **Tương tác hệ thống:** OS 
* **Trực quan hóa nâng cao:** Microsoft Power BI

---

## Hướng dẫn cài đặt & sử dụng

### 1. Yêu cầu hệ thống
* Đảm bảo máy tính đã cài đặt **Python 3.12**.

### 2. Cài đặt
Clone repository này về máy và cài đặt các thư viện yêu cầu:

```bash
# Clone dự án
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)

# Di chuyển vào thư mục dự án
cd your-repo-name

# Cài đặt các thư viện cần thiết
pip install pandas matplotlib
```

### 3. Chạy ứng dụng
```bash
#Chạy tập tin gốc để mở dữ án
python main.py
```

---

## Trực quan hóa dữ liệu với Power BI

Để nâng cao khả năng phân tích và ra quyết định, hệ thống kết hợp sức mạnh xử lý dữ liệu của Python với khả năng trình bày của Power BI. 

### Quy trình tích hợp:
Dữ liệu thô sau khi được Python làm sạch, chuẩn hóa sẽ được xuất ra file `cleaned_tlu.csv`. File này được Import vào Power BI Desktop (thông qua Text/CSV connector) để xây dựng Dashboard.

### Các biểu đồ phân tích trên Dashboard:
* **Card:** Cung cấp thông tin tổng quan của dữ liệu (Điểm số trung bình toàn khóa, Tổng số môn, Tổng số sinh viên).
* **Bar chart:** Phân tích và so sánh điểm số trung bình của từng môn học (Lập trình C++, Kiến trúc máy tính,...)].
* **Pie chart:** Phân tích tỷ lệ phần trăm sinh viên theo từng mức xếp loại (A, B, C, D, F).
* **Line chart:** Theo dõi xu hướng, tổng số sinh viên theo mức xếp loại qua các kỳ học (từ kỳ 1 đến kỳ 4).
* **Column chart:** Phân tích tổng số sinh viên theo kết quả (Đạt / Học lại) của từng kỳ học.

**[Xem Dashboard Power BI Trực Tuyến](https://app.powerbi.com/links/4JunFCA_KB?ctid=fc0bdaaf-292e-45cc-b51f-872867f9c981&pbi_source=linkShare)**

---

## Cấu trúc thư mục
```text
BTL_root/
  config/
  cong_cu/
  data/
  gd/
  services/
  state/
  requirements.txt
```

## Trích dẫn
Nếu bạn sử dụng repository này, vui lòng trích dẫn:

```bibtex
@misc{nckh3dface2026,
  title        = {BTL: hệ thống đánh giá sinh viên trường đại học Thăng Long},
  author       = {Huynh Hai Nam and Le Nguyen Nhat Huy and Nguyen Hong Son and Le Quang Khai},
  year         = {2025},
  howpublished = {GitHub repository},
  url          = {https://github.com/huylee733/Student-grades-management-system.git}
}
```
