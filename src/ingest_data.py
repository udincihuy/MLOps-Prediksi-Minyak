import yfinance as yf
import pandas as pd
import os

def ingest_data():
    # 1. Download data baru
    data = yf.download("CL=F", period="30d", interval="1d")


    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.reset_index(inplace=True)

    filename = "data/raw/oil.csv"
    os.makedirs("data/raw", exist_ok=True)

    if os.path.exists(filename):
        # 2. Tambahkan parse_dates agar data lama dibaca sebagai waktu, bukan teks
        existing = pd.read_csv(filename, parse_dates=["Date"])

        # 3. Gabung & hapus duplikat
        data = pd.concat([existing, data])
        
        # Pastikan kolom Date di data baru juga bertipe datetime sebelum drop_duplicates
        data["Date"] = pd.to_datetime(data["Date"])
        data = data.drop_duplicates(subset=["Date"], keep="last")

    # 4. Sekarang sort_values tidak akan error karena tipenya sudah seragam
    data = data.sort_values(by="Date")

    data.to_csv(filename, index=False)
    print(f"[INFO] Data berhasil diperbarui dan disimpan di {filename}")

if __name__ == "__main__":
    ingest_data()