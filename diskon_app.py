from pathlib import Path
import tkinter as tk
from tkinter import messagebox

def hitung_total():
    nama = entry_nama.get().strip()
    
    # Validasi input nominal belanja
    try:
        total_belanja = float(entry_belanja.get().strip())
        if total_belanja < 0:
            messagebox.showerror("Error", "Nominal total belanja tidak boleh negatif!")
            return
    except ValueError:
        messagebox.showerror("Error", "Masukkan nominal belanja dalam bentuk angka yang valid!")
        return

    # 1. Hitung Diskon Berdasarkan Total Belanja
    persen_diskon_belanja = 0
    if total_belanja < 100000:
        persen_diskon_belanja = 0
    elif 100000 <= total_belanja <= 500000:
        persen_diskon_belanja = 10
    else:  # total_belanja > 500000
        persen_diskon_belanja = 20

    diskon_belanja = total_belanja * (persen_diskon_belanja / 100)
    harga_setelah_diskon_belanja = total_belanja - diskon_belanja

    # 2. Tambahan Diskon Member (10% dari harga setelah diskon belanja)
    persen_diskon_member = 0
    diskon_member = 0
    if var_member.get() == 1:
        persen_diskon_member = 10
        diskon_member = harga_setelah_diskon_belanja * 0.10

    # Total Bayar Akhir
    total_bayar = harga_setelah_diskon_belanja - diskon_member

    # Format Teks Output / Rincian Struk
    nama_display = nama if nama else "-"
    hasil_text = (
        f"Rincian Pembayaran ({nama_display}):\n"
        f"----------------------------------------\n"
        f"Total Awal              : Rp {total_belanja:,.0f}\n"
        f"Diskon Belanja ({persen_diskon_belanja}%)   : Rp {diskon_belanja:,.0f}\n"
        f"Diskon Member ({persen_diskon_member}%)    : Rp {diskon_member:,.0f}\n"
        f"----------------------------------------\n"
        f"TOTAL BAYAR             : Rp {total_bayar:,.0f}"
    )

    # Tampilkan di area output
    lbl_hasil.config(text=hasil_text)

root = tk.Tk()
root.title("halo lek halo")
root.geometry("420x450")
root.resizable(False, False)
root.configure(bg="#AF4C91")

# Styling Sederhana
font_title = ("Mokoto", 12, "bold")
font_label = ("Mokoto", 10)
warna_background = "#F4EEF6"  # rgb(244, 238, 246)
warna_panel = "#FFFFFF"  # rgb(255, 255, 255)
warna_aksen = "#AF4C91"  # rgb(175, 76, 145)
root.configure(bg=warna_background)

# Header dan logo
frame_header = tk.Frame(root, bg=warna_background)
frame_header.pack(pady=(12, 8))

logo_path = Path(__file__).with_name("kranjang-removebg-preview.png")
logo_image = tk.PhotoImage(file=str(logo_path))
logo_image = logo_image.subsample(max(1, logo_image.width() // 58), max(1, logo_image.height() // 58))
logo = tk.Label(frame_header, image=logo_image, bg=warna_background)
logo.pack(side="left", padx=(0, 10))

lbl_title = tk.Label(frame_header, text="DISCOUNT", font=font_title, bg=warna_background)
lbl_title.pack(side="left")

# Frame Form Input
frame_input = tk.Frame(root, padx=10, pady=10, bg=warna_panel)
frame_input.pack(fill="x", padx=15)

# Input Nama Pembeli
lbl_nama = tk.Label(frame_input, text="Nama Pembeli :", font=font_label, bg=warna_panel)
lbl_nama.grid(row=0, column=0, sticky="w", pady=5)
entry_nama = tk.Entry(frame_input, width=30, font=font_label, bg=warna_panel)
entry_nama.grid(row=0, column=1, pady=5)

# Input Total Belanja
lbl_belanja = tk.Label(frame_input, text="Total Belanja :", font=font_label, bg=warna_panel)
lbl_belanja.grid(row=1, column=0, sticky="w", pady=5)
entry_belanja = tk.Entry(frame_input, width=30, font=font_label, bg=warna_panel)
entry_belanja.grid(row=1, column=1, pady=5)

# Checkbox Member
var_member = tk.IntVar()
chk_member = tk.Checkbutton(
    frame_input, 
    text="ndue member ta ga? (Diskon tambahan 10%)", 
    variable=var_member, 
    font=font_label,
    bg=warna_panel,
    activebackground=warna_panel
)
chk_member.grid(row=2, column=0, columnspan=2, sticky="w", pady=10)

# tombol hitung total
btn_hitung = tk.Button(
    root, 
    text="HITUNG TOTAL", 
    command=hitung_total, 
    bg=warna_aksen,
    fg="white", 
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)
btn_hitung.pack(pady=10)

# Area Output Rincian
frame_output = tk.LabelFrame(root, text=" Struk Pembayaran ", font=("Arial", 10, "bold"), padx=10, pady=10, bg=warna_panel)
frame_output.pack(fill="both", expand=True, padx=15, pady=10)

lbl_hasil = tk.Label(frame_output, text="MASUKIN-MASUKIN", font=("Courier", 9), justify="left", anchor="nw", bg=warna_panel)
lbl_hasil.pack(fill="both", expand=True)

# Jalankan Aplikasi
root.mainloop()