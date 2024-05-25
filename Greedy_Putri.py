import tkinter as tk
from tkinter import messagebox

# Dataset
dataset = [
    {"Nilai uang": 100, "Hasil greedy": [1, 0, 0, 0]},
    {"Nilai uang": 200, "Hasil greedy": [0, 1, 0, 0]},
    {"Nilai uang": 300, "Hasil greedy": [1, 1, 0, 0]},
    {"Nilai uang": 400, "Hasil greedy": [0, 2, 0, 0]},
    {"Nilai uang": 500, "Hasil greedy": [0, 0, 1, 0]},
    {"Nilai uang": 600, "Hasil greedy": [1, 1, 1, 0]},
    {"Nilai uang": 700, "Hasil greedy": [2, 1, 1, 0]},
    {"Nilai uang": 800, "Hasil greedy": [3, 1, 1, 0]},
    {"Nilai uang": 900, "Hasil greedy": [4, 1, 1, 0]},
    {"Nilai uang": 1000, "Hasil greedy": [0, 0, 0, 1]},
    {"Nilai uang": 1100, "Hasil greedy": [1, 0, 1, 1]},
    {"Nilai uang": 1200, "Hasil greedy": [2, 0, 1, 1]},
    {"Nilai uang": 1300, "Hasil greedy": [3, 0, 1, 1]},
    {"Nilai uang": 1400, "Hasil greedy": [4, 0, 1, 1]},
    {"Nilai uang": 1500, "Hasil greedy": [5, 0, 1, 1]},
    {"Nilai uang": 1600, "Hasil greedy": [6, 0, 1, 1]},
    {"Nilai uang": 1700, "Hasil greedy": [7, 0, 1, 1]},
    {"Nilai uang": 1800, "Hasil greedy": [8, 0, 1, 1]},
    {"Nilai uang": 1900, "Hasil greedy": [9, 0, 1, 1]},
    {"Nilai uang": 2000, "Hasil greedy": [10, 0, 1, 1]}
]

def hitung_kembalian(denominasi_koin, nilai_kembalian):
    kembalian = [0, 0, 0, 0]  # Inisialisasi jumlah koin untuk setiap denominasi
    sisa_nilai = nilai_kembalian

    for i, denom in enumerate(reversed(denominasi_koin)):
        jumlah_koin = min(sisa_nilai // denom, dataset[nilai_kembalian // 100 - 1]["Hasil greedy"][3 - i])
        kembalian[3 - i] = jumlah_koin
        sisa_nilai -= jumlah_koin * denom

    if sisa_nilai != 0:
        return "Tidak ada kembalian yang tepat untuk nilai tersebut."
    else:
        return kembalian

def hitung_kembalian_dan_tampilkan():
    nilai = int(entry_nilai_kembalian.get())
    hasil_kembalian = hitung_kembalian([100, 200, 500, 1000], nilai)
    messagebox.showinfo("Hasil", f"Nilai Tukar {nilai} Rupiah:\nJumlah koin 100 Rupiah: {hasil_kembalian[0]}\nJumlah koin 200 Rupiah: {hasil_kembalian[1]}\nJumlah koin 500 Rupiah: {hasil_kembalian[2]}\nJumlah koin 1000 Rupiah: {hasil_kembalian[3]}")

#GUI
root = tk.Tk()
root.title("Penghitung Kembalian")

label_nilai_kembalian = tk.Label(root, text="Masukkan Nilai uang (Rp) : ")
label_nilai_kembalian.pack()

entry_nilai_kembalian = tk.Entry(root)
entry_nilai_kembalian.pack()

tombol_hitung = tk.Button(root, text="Hitung Kembalian", command=hitung_kembalian_dan_tampilkan)
tombol_hitung.pack()

root.mainloop()