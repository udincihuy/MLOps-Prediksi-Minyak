import pandas as pd

def preprocess():
    file = "data/raw/oil.csv"

    try:
        data = pd.read_csv(file)
    except:
        print("Data tidak ditemukan!")
        return

    # ===== CLEANING =====
    data = data.dropna()
    data = data.drop_duplicates(subset=["Date"])

    # format tanggal
    data['Date'] = pd.to_datetime(data['Date'])

    # sorting (WAJIB sebelum lag)
    data = data.sort_values(by="Date")

    # ===== FEATURE ENGINEERING =====
    data['lag1'] = data['Close'].shift(1)
    data['lag2'] = data['Close'].shift(2)

    # 🔥 TARGET (prediksi besok)
    data['target'] = data['Close'].shift(-1)

    # hapus NaN akibat shift
    data = data.dropna()

    # simpan
    data.to_csv("data/processed.csv", index=False)

    print("[INFO] Preprocessing selesai, data siap training!")

if __name__ == "__main__":
    preprocess()