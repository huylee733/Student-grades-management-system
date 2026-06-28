import matplotlib.pyplot as plt
import pandas as pd

def plot_score_histogram(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df["Diem_So"], bins=10, color='skyblue', edgecolor='black')
    plt.title("Phân bố điểm số sinh viên")
    plt.xlabel("Điểm số")
    plt.ylabel("Số lượng")
    plt.show()

def plot_credit_score_scatter(df):
    plt.figure(figsize=(8, 5))
    plt.scatter(df["So_Tin_Chi"], df["Diem_So"], color='coral', alpha=0.7)
    plt.title("Tương quan Số tín chỉ - Điểm số")
    plt.xlabel("Số tín chỉ")
    plt.ylabel("Điểm số")
    plt.xticks(df["So_Tin_Chi"].unique())
    plt.grid(True, linestyle='--')
    plt.show()

def plot_avg_score_by_semester(df):
    plt.figure(figsize=(8, 5))
    if 'Ky_Hoc' not in df.columns: return 
    avg_data = df.groupby("Ky_Hoc")["Diem_So"].mean()
    avg_data.plot(kind="bar", color='lightgreen', edgecolor='black')
    plt.title("Điểm trung bình theo Kỳ học")
    plt.show()

def plot_pie_chart(df):
    if df is None or df.empty:
        return
    counts = df['Xep_Loai'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Tỷ lệ Xếp loại Sinh viên")
    plt.show()

def plot_score_trend_line(df):
    plt.figure(figsize=(8, 5))
    if 'Ky_Hoc' not in df.columns: return
    trend_data = df.groupby("Ky_Hoc")["Diem_So"].mean().sort_index()
    plt.plot(trend_data.index, trend_data.values, marker='o', linestyle='-', color='purple')
    plt.title("Xu hướng học tập qua các kỳ")
    plt.grid(True)
    plt.show()