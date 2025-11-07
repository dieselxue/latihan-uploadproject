import tkinter as tk
from tkinter import ttk
data_siswa = []
def buka_halaman2():
    halaman2.tkraise()
    tampilkan_data()
def buka_halaman3():
    halaman3.tkraise()
def kembali_ke_halaman1():
    halaman1.tkraise()
def simpan_data():
    nama = entry_nama.get()
    kelas = entry_kelas.get()
    alamat = entry_alamat.get()
    if nama and kelas and alamat:
        data_siswa.append({"nama": nama, "kelas": kelas, "alamat": alamat})
        entry_nama.delete(0, tk.END)
        entry_kelas.delete(0, tk.END)
        entry_alamat.delete(0, tk.END)
        label_status.config(text="Data berhasil disimpan!")
    else:
        label_status.config(text="Semua kolom harus diisi!")
def tampilkan_data():
    for i in tree.get_children():
        tree.delete(i)
    for s in data_siswa:
        tree.insert("", tk.END, values=(s["nama"], s["kelas"], s["alamat"]))
def cari_data():
    keyword = entry_cari.get().lower()
    for i in tree_cari.get_children():
        tree_cari.delete(i)
    for s in data_siswa:
        if keyword in s["nama"].lower():
            tree_cari.insert("", tk.END, values=(s["nama"], s["kelas"], s["alamat"]))
window = tk.Tk()
window.title("Aplikasi Data Siswa")
window.geometry("400x350")
halaman1 = ttk.Frame(window)
halaman2 = ttk.Frame(window)
halaman3 = ttk.Frame(window)
for frame in (halaman1, halaman2, halaman3):
    frame.grid(row=0, column=0, sticky='nsew')
ttk.Label(halaman1, text="Nama:").pack()
entry_nama = ttk.Entry(halaman1)
entry_nama.pack()
ttk.Label(halaman1, text="Kelas:").pack()
entry_kelas = ttk.Entry(halaman1)
entry_kelas.pack()
ttk.Label(halaman1, text="Alamat:").pack()
entry_alamat = ttk.Entry(halaman1)
entry_alamat.pack()
ttk.Button(halaman1, text="Simpan Data", command=simpan_data).pack(pady=5)
label_status = ttk.Label(halaman1, text="")
label_status.pack()
ttk.Button(halaman1, text="Lihat Data", command=buka_halaman2).pack(side=tk.LEFT, padx=5)
ttk.Button(halaman1, text="Cari Data", command=buka_halaman3).pack(side=tk.LEFT, padx=5)
kolom = ("Nama", "Kelas", "Alamat")
tree = ttk.Treeview(halaman2, columns=kolom, show="headings", height=10)
for kol in kolom:
    tree.heading(kol, text=kol)
tree.pack(pady=5)
ttk.Button(halaman2, text="Kembali", command=kembali_ke_halaman1).pack()
ttk.Label(halaman3, text="Masukkan Nama:").pack()
entry_cari = ttk.Entry(halaman3)
entry_cari.pack(pady=5)
ttk.Button(halaman3, text="Cari", command=cari_data).pack()
kolom_cari = ("Nama", "Kelas", "Alamat")
tree_cari = ttk.Treeview(halaman3, columns=kolom_cari, show="headings", height=8)
for kol in kolom_cari:
    tree_cari.heading(kol, text=kol)
tree_cari.pack(pady=5)
ttk.Button(halaman3, text="Kembali", command=kembali_ke_halaman1).pack()
halaman1.tkraise()
window.mainloop()
