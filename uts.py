# Pemograman Data Science

# NIM : 10124190
# Nama : Rizkya Gusnaldy Kalia
# Kelas : IF-5

import pandas as pd
import matplotlib.pylab as plt

# Mengambil data dari file Excel
df_awal = pd.read_excel('data_set.xlsx')

# Menghapus data duplikat jika ada dan menghapus baris kosong
df_bersih = df_awal.drop_duplicates()
df = df_bersih.dropna(subset=['NIM','KELAS','KEHADIRAN','TUGAS','UTS','UAS'])

# ---------------------------------------------------------------------------------------
print('\n')

# Nilai kehadiran
df['nilai_kehadiran'] = (df['KEHADIRAN'] / 16*100) * 5/100

# Tugas
df['nilai_tugas'] = df['TUGAS'] * 20/100

# UTS
df['nilai_uts'] = df['UTS'] * 35/100

# UAS
df['nilai_uas'] = df['UAS'] * 40/100

# Nilai Akhir
df['nilai_akhir'] = df['nilai_kehadiran'] + df['nilai_tugas'] + df['nilai_uts'] + df['nilai_uas']

# Menampilkan Data dengan nilai_akhir
print(df[['NIM', 'KELAS', 'KEHADIRAN', 'TUGAS', 'UTS' , 'UAS', 'nilai_akhir']].head(5))

# ---------------------------------------------------------------------------------------
print('\n')

# Index nilai akhir
df['index'] = df['nilai_akhir'].apply(lambda x: 'A' if x >= 80 else ('B' if x >= 68 else ('C' if x >= 56 else ('D' if x >= 45 else 'E'))))

# Menampilkan Data dengan nilai_akhir dan index
print(df[['NIM', 'KELAS', 'KEHADIRAN', 'TUGAS', 'UTS' , 'UAS', 'nilai_akhir', 'index']].head(5))

# ---------------------------------------------------------------------------------------
print('\n')

# Simpan hasil ke file Excel baru
df.to_excel('data_set_nilai.xlsx')

# ---------------------------------------------------------------------------------------

# Membuat pie chart berdasarkan index nilai_akhir
plt.figure(figsize=(10,6))
plt.pie(df['index'].value_counts(), labels=df['index'].value_counts().index, autopct='%1.1f%%')
plt.tight_layout()
plt.show()