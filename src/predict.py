import mlflow
import pandas as pd

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_registry_uri("sqlite:///mlflow.db")

model = mlflow.pyfunc.load_model("models:/harga_minyak_model/Production")

data = pd.DataFrame({
    "lag1": [100],
    "lag2": [98],
    "ma3": [99]
})

pred = model.predict(data)

print("Prediksi harga minyak:", pred)