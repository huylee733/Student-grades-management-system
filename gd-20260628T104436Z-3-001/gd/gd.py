import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os
import webbrowser
import matplotlib.pyplot as plt

from config.app_config import DATA_PATH
from cong_cu.data_ut import load_and_clean_data
from services.diemsv import (
    plot_score_histogram, 
    plot_credit_score_scatter,
    plot_avg_score_by_semester, 
    plot_pie_chart,
    plot_score_trend_line
)
app_data = None
app_filtered_data = None

def run_app():
    global app_data, app_filtered_data
    root = tk.Tk()
    root.title("Hệ thống Quản lý Điểm Sinh Viên")
    root.geometry("1200x700")
    try:
        app_data = load_and_clean_data(DATA_PATH)
        if 'Ma_Hoc_Phan' not in app_data.columns:
            app_data['Ma_Hoc_Phan'] = '' 
        app_filtered_data = app_data.copy()
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không đọc được dữ liệu: {e}")
        return
    def update_table(data):
        for item in tree.get_children():
            tree.delete(item)
        for _, row in data.iterrows():
            tree.insert("", "end", values=list(row))
    def filter_data():
        keyword = search_entry.get()
        if keyword:
            global app_filtered_data
            mask = app_data['Ten_Mon'].str.contains(keyword, case=False, na=False) | \
                   app_data['Ma_SV'].str.contains(keyword, case=False, na=False) | \
                   app_data['Ma_Hoc_Phan'].str.contains(keyword, case=False, na=False)
            app_filtered_data = app_data[mask]
        else:
            app_filtered_data = app_data.copy()
        update_table(app_filtered_data)
    def save_to_csv():
        app_data.to_csv(DATA_PATH, index=False)
    def open_admin_window():
        win = tk.Toplevel(root)
        win.title("Thêm/Xóa Dữ Liệu")
        win.geometry("400x550")
        fields = ["Ma_SV", "Ma_Hoc_Phan", "Ten_Mon", "So_Tin_Chi", "Diem_So", "Ky_Hoc"]
        entries = {}
        tk.Label(win, text="NHẬP THÔNG TIN", font=("Arial", 12, "bold"), fg="blue").pack(pady=10)
        for f in fields:
            frame = tk.Frame(win)
            frame.pack(fill="x", padx=20, pady=5)
            tk.Label(frame, text=f, width=15, anchor="w").pack(side=tk.LEFT)
            e = tk.Entry(frame)
            e.pack(side=tk.RIGHT, expand=True, fill="x")
            entries[f] = e
        def add_record():
            try:
                global app_data, app_filtered_data
                new_row = {f: entries[f].get() for f in fields}
                new_row["So_Tin_Chi"] = int(new_row["So_Tin_Chi"])
                new_row["Diem_So"] = float(new_row["Diem_So"])
                new_row["Ky_Hoc"] = int(new_row["Ky_Hoc"])
                
                diem = new_row["Diem_So"]
                new_row["Ket_Qua"] = "Đạt" if diem >= 4.0 else "Học lại"
                
                if diem >= 8.5: new_row["Xep_Loai"] = 'A'
                elif diem >= 7.0: new_row["Xep_Loai"] = 'B'
                elif diem >= 5.5: new_row["Xep_Loai"] = 'C'
                elif diem >= 4.0: new_row["Xep_Loai"] = 'D'
                else: new_row["Xep_Loai"] = 'F'

                app_data.loc[len(app_data)] = new_row
                save_to_csv()    
                app_filtered_data = app_data.copy()
                update_table(app_filtered_data)
                messagebox.showinfo("OK", "Đã thêm dữ liệu!")
                win.destroy()
            except ValueError:
                messagebox.showerror("Lỗi", "Số tín chỉ, Điểm, Kỳ học phải là số!")
        def delete_record():
            global app_data, app_filtered_data
            selected = tree.selection()
            if not selected:
                messagebox.showwarning("Cảnh báo", "Chọn dòng cần xóa trước!")
                return
            vals = tree.item(selected[0])['values']
            ma_sv_xoa = str(vals[0])
            ma_hp_xoa = str(vals[1]) 
            confirm = messagebox.askyesno("Xác nhận", f"Xóa SV: {ma_sv_xoa} - Mã HP: {ma_hp_xoa}?")
            if confirm:
                idx = app_data[
                    (app_data['Ma_SV'].astype(str) == ma_sv_xoa) & 
                    (app_data['Ma_Hoc_Phan'].astype(str) == ma_hp_xoa)
                ].index
                app_data.drop(idx, inplace=True)
                app_data.reset_index(drop=True, inplace=True)
                save_to_csv()
                app_filtered_data = app_data.copy()
                update_table(app_filtered_data)
                messagebox.showinfo("OK", "Đã xóa!")
                win.destroy()

        btn_frame = tk.Frame(win, pady=20)
        btn_frame.pack()
        tk.Button(btn_frame, text="Lưu", bg="green", fg="white", command=add_record).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Xóa", bg="red", fg="white", command=delete_record).pack(side=tk.LEFT, padx=10)
    top_frame = tk.Frame(root, pady=10)
    top_frame.pack(fill="x", padx=10)
    tk.Label(top_frame, text="Tìm kiếm (Môn/SV/Mã HP):").pack(side=tk.LEFT)
    search_entry = tk.Entry(top_frame, width=30)
    search_entry.pack(side=tk.LEFT, padx=5)
    tk.Button(top_frame, text="Lọc", command=filter_data).pack(side=tk.LEFT)
    tk.Button(top_frame, text="Thêm/Xóa dữ liệu", bg="orange", command=open_admin_window).pack(side=tk.RIGHT)
    mid_frame = tk.Frame(root)
    mid_frame.pack(fill="both", expand=True, padx=10, pady=5)
    cols = ['Ma_SV', 'Ma_Hoc_Phan', 'Ten_Mon', 'So_Tin_Chi', 'Diem_So', 'Ky_Hoc', 'Xep_Loai', 'Ket_Qua']
    tree = ttk.Treeview(mid_frame, columns=cols, show="headings")
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center") 
    tree.pack(fill="both", expand=True)
    update_table(app_data)
    bot_frame = tk.Frame(root, bg="#f0f0f0", pady=10, bd=2, relief="groove")
    bot_frame.pack(fill="x", side=tk.BOTTOM)
    tk.Label(bot_frame, text="BIỂU ĐỒ:", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=10)
    charts = [
        ("Phân bố Điểm", plot_score_histogram),
        ("Scatter Tín chỉ", plot_credit_score_scatter),
        ("Bar Kỳ học", plot_avg_score_by_semester),
        ("Tỷ lệ Xếp loại", plot_pie_chart),
        ("Xu hướng Line", plot_score_trend_line),
    ]
    for name, func in charts:
        tk.Button(bot_frame, text=name, command=lambda f=func: f(app_filtered_data)).pack(side=tk.LEFT, padx=5)
    def open_powerbi_dashboard():
        url = "https://app.powerbi.com/links/4JunFCA_KB?ctid=fc0bdaaf-292e-45cc-b51f-872867f9c981&pbi_source=linkShare"
        webbrowser.open(url)
    btn_pbi = tk.Button(bot_frame, 
                        text="Dashboard Power BI", 
                        bg="#F2C811", fg="black", font=("Arial", 10, "bold"), 
                        command=open_powerbi_dashboard)
    btn_pbi.pack(side=tk.RIGHT, padx=20)
    root.mainloop()