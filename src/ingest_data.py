import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def ingest_data():
    # ambil data 1 hari terakhir
    data = yf.download("CL=F", period="30d", interval="1d")

    data.reset_index(inplace=True)

    # ambil tanggal hari ini
    today = datetime.now().strftime("%Y-%m-%d")

    # nama file per hari
    filename = f"data/raw/oil_{today}.csv"

    os.makedirs("data/raw", exist_ok=True)

    # kalau file sudah ada → append (biar gak overwrite)
    if os.path.exists(filename):
        existing = pd.read_csv(filename)
        data = pd.concat([existing, data]).drop_duplicates()

    data.to_csv(filename, index=False)

    print(f"[INFO] Data harian disimpan: {filename}")

if __name__ == "__main__":
    ingest_data()