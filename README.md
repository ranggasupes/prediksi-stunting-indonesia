# Analisis dan Prediksi Tingkat Stunting di Indonesia Menggunakan Machine Learning (Random Forest & SVR)

Repositori ini berisi implementasi proyek komputasi Machine Learning untuk menganalisis dan memprediksi tingkat prevalensi stunting di Indonesia berdasarkan indikator kesehatan dan sosial ekonomi. Proyek ini dikembangkan menggunakan bahasa pemrograman Python dengan pendekatan regresi non-linear untuk menangkap pola kompleks dalam data kesehatan masyarakat.

Proyek ini disusun sebagai bagian dari tugas mata kuliah Statistik dan Probabilitas.

---

## 📌 Latar Belakang Studi

Stunting merupakan salah satu permasalahan kesehatan kronis di Indonesia yang dipengaruhi oleh banyak faktor multidimensi, seperti status gizi, sanitasi, akses air bersih, kemiskinan, dan tingkat pendidikan masyarakat.

Hubungan antar variabel tersebut bersifat non-linear dan kompleks, sehingga pendekatan statistik sederhana sering tidak mampu memberikan prediksi yang optimal. Oleh karena itu, proyek ini mengimplementasikan algoritma Machine Learning berbasis regresi, yaitu Random Forest Regressor dan Support Vector Regression (SVR), untuk melakukan analisis prediktif terhadap prevalensi stunting.

---

## 📊 Dataset dan Variabel Penelitian

Dataset yang digunakan merupakan data sekunder yang terdiri dari indikator kesehatan dan sosial ekonomi di berbagai provinsi di Indonesia, meliputi:

- Gizi Buruk (%)
- Gizi Kurang (%)
- Sanitasi Layak (%)
- Air Minum Layak (%)
- Kemiskinan (%)
- Indeks Pembangunan Manusia (IPM)
- Tahun Observasi
- Stunting (%)

---

## ⚙️ Alur Kerja Machine Learning (Pipeline)

Sistem prediksi dalam repositori ini dibangun melalui tahapan berikut:

### 1. Prapemrosesan Data
- Menghapus data yang memiliki nilai kosong (missing value)
- Memastikan konsistensi format data numerik

### 2. Rekayasa Fitur
- Menggunakan variabel sosial ekonomi sebagai fitur prediktor
- Menentukan Stunting (%) sebagai target prediksi

### 3. Pembagian Dataset
- Training Set: 80%
- Testing Set: 20%

### 4. Normalisasi Data
- Menggunakan StandardScaler untuk menyamakan skala fitur
- Khusus digunakan pada model SVR

### 5. Pelatihan Model Machine Learning
Dua algoritma digunakan:
- Random Forest Regressor (ensemble-based learning)
- Support Vector Regression (SVR) dengan kernel RBF

### 6. Evaluasi Model
Model dibandingkan menggunakan metrik:
- Mean Absolute Error (MAE)
- R-Squared (R² Score)

Model terbaik dipilih berdasarkan nilai R² tertinggi.

### 7. Prediksi Multitahun
Model digunakan untuk memprediksi tren stunting pada tahun 2024–2027 di setiap provinsi dengan pendekatan simulasi perubahan indikator.

### 8. Visualisasi Data
Hasil prediksi divisualisasikan menggunakan Matplotlib dalam bentuk:
- Grafik perbandingan antar provinsi
- Bar chart prediksi stunting tahun 2027

---

## 📈 Output Sistem

Output dari sistem ini berupa:

- File hasil prediksi: `hasil_prediksi_stunting.xlsx`
- Grafik visualisasi prediksi stunting per provinsi
- Perbandingan performa model Machine Learning

---

## 🛠 Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## 🎯 Tujuan Proyek

- Menganalisis faktor-faktor yang mempengaruhi stunting
- Membangun model prediktif berbasis Machine Learning
- Membandingkan performa algoritma Random Forest dan SVR
- Menghasilkan prediksi berbasis data multi-tahun

---

## ⚠️ Catatan

Model yang digunakan bersifat prediktif berbasis data historis dan tidak menggantikan analisis medis atau kebijakan resmi pemerintah. Hasil prediksi digunakan untuk simulasi dan analisis akademik.

---