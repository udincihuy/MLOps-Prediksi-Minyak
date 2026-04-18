# Sistem Prediksi Harga Minyak Berbasis MLOps

## Struktur Direktori

Berikut struktur proyek yang digunakan:

```text
MLOps-Sistem-Prediksi-harga-minyak/
├── data/           → Berkaitan dengan data yang diambil (data ada versioningnya)
│   ├── raw/        → Data mentah dari API
│   └── processed/  → Data yang sudah dibersihkan
├── models/         → Penyimpanan model hasil training
├── notebooks/      → Eksperimen dan Exploratory Data Analysis (EDA)
├── src/            → Source code utama (data ingestion, training, dll)
│   └── hello.py    → Script coba-coba saat setup
├── config/         → File konfigurasi (parameter, setting, dsb)
├── tests/          → Unit testing
├── docs/           → Dokumentasi tambahan
├── .gitignore      → File untuk mengabaikan file/folder tertentu di Git
├── LICENSE         → Lisensi proyek
└── README.md       → Dokumentasi utama proyek
```

Lk - 04
1. Mengambil Data (Data Ingestion)
Jalankan skrip ini untuk menarik data terbaru dan menyimpannya di folder data/raw/.


python src/ingest_data.py
2. Membersihkan Data (Preprocessing)
Jalankan skrip ini untuk membuang data yang rusak/kosong dan merapikan formatnya. Hasilnya akan muncul di folder data/processed/.


python src/preprocess.py
 
Penjelasan File Utama
ingest_data.py: Bertugas sebagai "pengumpul data". Skrip ini memastikan data masuk ke sistem dengan aman tanpa mengubah isi aslinya.

preprocess.py: Bertugas sebagai "penyaring data". Skrip ini melakukan pembersihan (cleaning) seperti menghapus nilai kosong dan menyeragamkan format teks.

traffic_data_raw.csv: Sampel data yang berisi informasi jumlah kendaraan, waktu, dan kondisi cuaca di lokasi sensor.## Menjalankan skrip pengumpul data (singkat)
Prasyarat: Python dan paket `yfinance`, `pandas`.

Jalankan:
```
python src\ingest_data.py
```

Output: file di `data/raw/` bernama `oil_YYYY-MM-DD.csv`.
