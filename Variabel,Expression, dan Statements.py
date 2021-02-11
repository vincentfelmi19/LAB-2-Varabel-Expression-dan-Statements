# Nama: Vincentsius Felmi Ajang
# Universitas Kristen Duta Wacana
'''
Memberikan nilai pada variabel Referensi Modul praktikum 2 (2.5.2)
Nindy adalah seorang mahasiswa baru di Universitas Kristen Duta Wacana, Nindy ingin
mencatat sisa uang yang ia miliki, karena ia baru saja berbelanja perabotan untuk kostnya. 
Perabotan yang ia telah beli adalah Meja, Ranjang, Lemari, dan Kursi.

'''

'''
Input : uang_modal; harga_meja; harga_ranjang; harga_lemari

Proses : uang_total_belanja; sisa_uang

Output : sisa_uang

'''

# Input
uang_modal = float(input("Masukkan uang modal : "))
harga_meja = float(input("Masukkan harga meja : "))
harga_ranjang = float(input("Masukkan harga ranjang : "))
harga_lemari = float(input("Masukkan harga lemari : "))

# Proses
uang_total_belanja = harga_meja + harga_ranjang + harga_lemari
sisa_uang = uang_modal - uang_total_belanja

# Output
print("Sisa uang Nindy = Rp. %.2f"%(sisa_uang))