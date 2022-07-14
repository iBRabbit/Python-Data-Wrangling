import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

# Akses kolom
print(csv_data.head())
print(csv_data["Age"])
print(csv_data["CustomerID"])

print(csv_data.iloc[5]) # Akses Baris