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