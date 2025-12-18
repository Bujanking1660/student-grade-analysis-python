# Student Grade Analysis - UTS Pemrograman Dasar Sains Data 📊

Proyek ini adalah implementasi pengolahan data nilai mahasiswa menggunakan library **Pandas** untuk manipulasi data dan **Matplotlib** untuk visualisasi. Proyek ini dikerjakan sebagai bagian dari Ujian Tengah Semester (UTS).

## 👤 Identitas Mahasiswa
- **Nama** : Rizkya Gusnaldy Kalia
- **NIM** : 10124190
- **Kelas** : IF-5

## 📝 Deskripsi Proyek
Program ini melakukan automasi pengolahan nilai mentah dari file Excel menjadi nilai akhir dan indeks huruf (A-E). Langkah-langkah yang dilakukan meliputi:
1. **Data Cleaning**: Menghapus data duplikat dan baris yang memiliki nilai kosong (NaN).
2. **Kalkulasi Nilai**: Menghitung Nilai Akhir berdasarkan bobot:
   - Kehadiran (5%)
   - Tugas (20%)
   - UTS (35%)
   - UAS (40%)
3. **Penentuan Indeks**: Mengonversi nilai akhir menjadi indeks A, B, C, D, atau E.
4. **Export Data**: Menyimpan hasil pengolahan ke file Excel baru (`data_set_nilai.xlsx`).
5. **Visualisasi**: Menampilkan persentase persebaran indeks nilai mahasiswa dalam bentuk *Pie Chart*.

## 🛠️ Teknologi yang Digunakan
- **Python 3.x**
- **Pandas**: Untuk manipulasi data (DataFrame).
- **Matplotlib**: Untuk visualisasi data (Pie Chart).
- **Openpyxl**: Engine untuk membaca/menulis file Excel.

## 🚀 Cara Menjalankan
1. Pastikan file `data_set.xlsx` berada dalam folder yang sama dengan skrip Python.
2. Instal library yang dibutuhkan:
 ```bash
 pip install pandas matplotlib openpyxl

```

3. Jalankan skrip:
```bash
python main.py

```



## 📊 Hasil Output

* File `data_set_nilai.xlsx` yang berisi tabel nilai lengkap dengan indeks.
* Grafik *Pie Chart* yang menunjukkan distribusi nilai mahasiswa di layar.

---

© 2025 Rizkya Gusnaldy Kalia - Universitas Komputer Indonesia

