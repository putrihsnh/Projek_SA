import tkinter as tk
from tkinter import messagebox

def sort_coins():
    coins = list(map(int, entry_coins.get().split()))
    coins.sort(reverse=True)
    entry_coins.delete(0, tk.END)
    entry_coins.insert(tk.END, ' '.join(map(str, coins)))

def calculate():
    try:
        uang = int(entry_uang.get())
        coins = list(map(int, entry_coins.get().split()))
        hasil = [0] * len(coins)

        for i, coin in enumerate(coins):
            hasil[i] = uang // coin
            uang %= coin

        result_text = "\n".join([f"Koin Rp {coins[i]} - an Sebanyak: {hasil[i]} keping" for i in range(len(coins))])
        messagebox.showinfo("Hasil Algoritma Greedy", result_text)
    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai yang valid")

root = tk.Tk()
root.title("Aplikasi penukaran uang coin ")

frame_coins = tk.Frame(root)
frame_coins.pack(pady=10)

label_coins = tk.Label(frame_coins, text="Masukkan jenis uang coin (Rp) : ")
label_coins.grid(row=0, column=0)

entry_coins = tk.Entry(frame_coins)
entry_coins.grid(row=0, column=1)

btn_sort_coins = tk.Button(frame_coins, text="Urutkan", command=sort_coins)
btn_sort_coins.grid(row=0, column=2)

label_amount = tk.Label(root, text="Masukkan nilai yang ingin dipecah (Rp) : ")
label_amount.pack()

entry_uang = tk.Entry(root)
entry_uang.pack()

btn_calculate = tk.Button(root, text="Hitung", command=calculate)
btn_calculate.pack()

root.mainloop()