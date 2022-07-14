'''
Menampilkan data dalam range tertentu

Setelah menampilkan suatu kelompok data, bagaimana jika ingin menampilkan data dari baris ke 5 sampai ke 20 dari suatu dataset? Untuk mengantisipasi hal tersebut, pandas juga bisa menampilkan data dalam range tertentu, baik range untuk baris saja, kolom saja, dan range untuk baris dan kolom.

Akses range pada suatu kolom dan baris tertentu, untuk mencobanya silahkan ketikkan kode di bawah ini :
'''

import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

print("Menampilkan data ke 5 sampai kurang dari 10 :")

print(csv_data["Age"].iloc[5:10])


