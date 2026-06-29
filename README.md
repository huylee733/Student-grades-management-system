# BÀI TẬP LỚN: Hệ thống quản lý sinh viên trường đại học Thăng Long

## Nhóm nghiên cứu
- **Đơn vị:** Trường Đại học Thăng Long
- **Giảng viên hướng dẫn:** ThS. Nguyễn Hùng Cường

- **Thành viên:**
- A49828 Nguyễn Hồng Sơn
- A49971 Lê Nguyễn Nhật Huy
- A56677 Lê Quang Khải
- A51575 Huỳnh Hải Nam

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

## Hướng dẫn Cài đặt & Sử dụng

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
