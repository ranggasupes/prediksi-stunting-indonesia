import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

print("Prediksi Stunting Indonesia")

df = pd.read_excel(
    "dataset_stunting_indonesia.xlsx"
)

print(df.head())

df = df.dropna(
    subset=["Stunting (%)"]
)

print("DATASET STUNTING INDONESIA")
print(f"Jumlah Data      : {len(df)}")
print(f"Jumlah Provinsi  : {df['Provinsi'].nunique()}")

FITUR = [
    "Gizi Buruk (%)",
    "Gizi Kurang (%)",
    "Sanitasi Layak (%)",
    "Air Minum Layak (%)",
    "Kemiskinan (%)",
    "IPM",
    "Tahun"
]

TARGET = "Stunting (%)"

X = df[FITUR]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = {
    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ),
    "SVR": SVR(
        kernel="rbf",
        C=100,
        gamma="scale"
    )
}

print("PERBANDINGAN MODEL")
print(f"{'Model':<20} {'MAE':>10} {'R2 Score':>10}")
print("-" * 45)

for nama, model in models.items():

    if nama == "SVR":
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"{nama:<20} {mae:>10.3f} {r2:>10.4f}")

    if r2 > best_r2:
        best_r2 = r2
        best_model = model
        best_model_name = nama

print()
print(f"Model Terbaik : {best_model_name}")
print(f"R2 Score      : {best_r2:.4f}")
print()

if best_model_name == "SVR":
    X_full = scaler.fit_transform(X)

    best_model = SVR(
        kernel="rbf",
        C=100,
        gamma="scale"
    )

    best_model.fit(X_full, y)

else:
    best_model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    best_model.fit(X, y)

    def prediksi_provinsi(nama_provinsi, tahun_prediksi=[2024, 2025, 2026, 2027]):

        data_prov = df[df["Provinsi"] == nama_provinsi].sort_values("Tahun")

        if data_prov.empty:
            return None

        terakhir = data_prov.iloc[-1].copy()
        stunting_terakhir = terakhir["Stunting (%)"]

        hasil = []

        for tahun in tahun_prediksi:

            fitur_prediksi = {
                "Gizi Buruk (%)": terakhir["Gizi Buruk (%)"] * 0.99,
                "Gizi Kurang (%)": terakhir["Gizi Kurang (%)"] * 0.99,
                "Sanitasi Layak (%)": min(100, terakhir["Sanitasi Layak (%)"] * 1.01),
                "Air Minum Layak (%)": min(100, terakhir["Air Minum Layak (%)"] * 1.01),
                "Kemiskinan (%)": terakhir["Kemiskinan (%)"] * 0.98,
                "IPM": terakhir["IPM"] * 1.005,
                "Tahun": tahun
            }

            X_pred = pd.DataFrame([fitur_prediksi])