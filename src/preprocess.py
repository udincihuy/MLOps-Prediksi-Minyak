import pandas as pd
import glob

def preprocess():
    files = glob.glob("data/raw/*.csv")

    if not files:
        print("Data tidak ditemukan!")
        return

    df_list = [pd.read_csv(f) for f in files]
    data = pd.concat(df_list, ignore_index=True)

    # ===== CLEANING =====
    data = data.dropna()
    data = data.drop_duplicates()

    # pastikan format tanggal
    data['Date'] = pd.to_datetime(data['Date'])

    # urutkan
    data = data.sort_values(by="Date")

    # ===== FEATURE ENGINEERING =====
    # lag (hari sebelumnya)
    data['lag1'] = data['Close'].shift(1)
    data['lag2'] = data['Close'].shift(2)

    # moving average
    data['ma3'] = data['Close'].rolling(3).mean()

    # hapus NaN akibat lag
    data = data.dropna()

    # simpan
    data.to_csv("data/processed.csv", index=False)

    print("[INFO] Preprocessing selesai, data siap training!")

if __name__ == "__main__":
    preprocess()