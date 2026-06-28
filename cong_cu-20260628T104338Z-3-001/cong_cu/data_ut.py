import pandas as pd
import os
DATA_PATH = 'raw_tlu.csv' 
def tinh_diem_chu(d):
    if d >= 8.5: return 'A'
    elif d >= 7.0: return 'B'
    elif d >= 5.5: return 'C'
    elif d >= 4.0: return 'D'
    else: return 'F'
def load_and_clean_data(filepath):
    if not os.path.exists(filepath):
        print(f"File {filepath} chưa tồn tại. Đang tạo mẫu...")
        df = pd.DataFrame({
            'Ma_SV': ['SV001', 'SV002', 'SV003'],
            'Ten_Mon': ['Tin đại cương', 'Giải tích 1', 'Triết học'],
            'So_Tin_Chi': [2, 3, 3],
            'Diem_So': [8.5, 3.0, 7.0],
            'Ky_Hoc': [1, 1, 2] 
        })
    else:
        df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()
    df['Diem_So'] = pd.to_numeric(df['Diem_So'], errors='coerce')
    df = df.dropna(subset=['Diem_So'])
    df = df[(df['Diem_So'] >= 0) & (df['Diem_So'] <= 10)]
    df['Xep_Loai'] = df['Diem_So'].apply(tinh_diem_chu)
    df['Ket_Qua'] = df['Diem_So'].apply(lambda x: 'Đạt' if x >= 4.0 else 'Học lại')
    df = df.drop(columns=['XepLoai', 'KetQua'], errors='ignore')
    output_path = os.path.join('cleaned_tlu.csv')
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Đã lưu dữ liệu làm sạch tại: {output_path}")
    return df