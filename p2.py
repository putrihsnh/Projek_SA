import tkinter as tk
from tkinter import messagebox

# Dataset
dataset = [
    {"Nilai Kembalian": 100, "Kombinasi Koin": [1, 0, 0, 0]},
    {"Nilai Kembalian": 200, "Kombinasi Koin": [0, 1, 0, 0]},
    {"Nilai Kembalian": 300, "Kombinasi Koin": [1, 1, 0, 0]},
    {"Nilai Kembalian": 400, "Kombinasi Koin": [0, 2, 0, 0]},
    {"Nilai Kembalian": 500, "Kombinasi Koin": [0, 0, 1, 0]},
    {"Nilai Kembalian": 600, "Kombinasi Koin": [1, 1, 1, 0]},
    {"Nilai Kembalian": 700, "Kombinasi Koin": [2, 1, 1, 0]},
    {"Nilai Kembalian": 800, "Kombinasi Koin": [3, 1, 1, 0]},
    {"Nilai Kembalian": 900, "Kombinasi Koin": [4, 1, 1, 0]},
    {"Nilai Kembalian": 1000, "Kombinasi Koin": [0, 0, 0, 1]},
    {"Nilai Kembalian": 1100, "Kombinasi Koin": [1, 0, 1, 1]},
    {"Nilai Kembalian": 1200, "Kombinasi Koin": [2, 0, 1, 1]},
    {"Nilai Kembalian": 1300, "Kombinasi Koin": [3, 0, 1, 1]},
    {"Nilai Kembalian": 1400, "Kombinasi Koin": [4, 0, 1, 1]},
    {"Nilai Kembalian": 1500, "Kombinasi Koin": [5, 0, 1, 1]},
    {"Nilai Kembalian": 1600, "Kombinasi Koin": [6, 0, 1, 1]},
    {"Nilai Kembalian": 1700, "Kombinasi Koin": [7, 0, 1, 1]},
    {"Nilai Kembalian": 1800, "Kombinasi Koin": [8, 0, 1, 1]},
    {"Nilai Kembalian": 1900, "Kombinasi Koin": [9, 0, 1, 1]},
    {"Nilai Kembalian": 2000, "Kombinasi Koin": [5, 0, 1, 1]}
]

def hitung_kembalian(denominasi_koin, nilai_kembalian):
    kembalian = [0, 0, 0, 0]  # Inisialisasi jumlah koin untuk setiap denominasi
    sisa_nilai = nilai_kembalian

    for i, denom in enumerate(reversed(denominasi_koin)):
        jumlah_koin = min(sisa_nilai // denom, dataset[nilai_kembalian // 100 - 1]["Kombinasi Koin"][3 - i])
        kembalian[3 - i] = jumlah_koin
        sisa_nilai -= jumlah_koin * denom

    if sisa_nilai != 0:
        return "Tidak ada kembalian yang tepat untuk nilai tersebut."
    else:
        return kembalian

def hitung_kembalian_dan_tampilkan():
    nilai = int(entry_nilai_kembalian.get())
    hasil_kembalian = hitung_kembalian([100, 200, 500, 1000], nilai)
    messagebox.showinfo("Hasil", f"Nilai kembalian {nilai} Rupiah:\nJumlah koin 100 Rupiah: {hasil_kembalian[0]}\nJumlah koin 200 Rupiah: {hasil_kembalian[1]}\nJumlah koin 500 Rupiah: {hasil_kembalian[2]}\nJumlah koin 1000 Rupiah: {hasil_kembalian[3]}")

# Buat GUI
root = tk.Tk()
root.title("Penghitung Kembalian")

label_nilai_kembalian = tk.Label(root, text="Masukkan Nilai Kembalian (dalam Rupiah):")
label_nilai_kembalian.pack()

entry_nilai_kembalian = tk.Entry(root)
entry_nilai_kembalian.pack()

tombol_hitung = tk.Button(root, text="Hitung Kembalian", command=hitung_kembalian_dan_tampilkan)
tombol_hitung.pack()

root.mainloop()