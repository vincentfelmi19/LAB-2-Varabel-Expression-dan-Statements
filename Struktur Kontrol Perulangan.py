# Nama: Vincentsius Felmi Ajang
# Universitas Kristen Duta Wacana
'''
Mencari jumlah huruf vokal, konsonan, dan angka dan referensi Modul Praktikum 5 (5.4) contoh 5.2
Buatlah sebuah program yang dapat mencari jumlah huruf vokal, konsonan, dan angka didalam suatu 
kalimat yang diberikan oleh user. Contoh:

    Ibu Aldi membeli 20 bungkus garam
        
        huruf vokal = 11
        huruf konsonan = 15
        angka = 2

'''

'''
Input : kalimat, huruf_vokal, huruf_konsonan, angka, jumlah_vokal, jumlah_konsonan, jumlah_angka

Proses : for isi in kalimat(elif isi in huruf_vokal, elif isi in huruf_konsonan, elif isi in angka)

Output : jumlah_vokal, jumlah_konsonan, jumlah_angka

'''

# Input
kalimat = input("Masukkan kalimat : ")
huruf_vokal = "AIUEOaiueo"
huruf_konsonan = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
angka = "0123456789"
jumlah_vokal = 0
jumlah_konsonan = 0
jumlah_angka = 0

# Proses
for isi in kalimat:
    if isi in huruf_vokal:
        jumlah_vokal += 1
    elif isi in huruf_konsonan:
        jumlah_konsonan += 1
    elif isi in angka:
        jumlah_angka += 1

# Output
print("Jumlah vokal = ", jumlah_vokal)
print("Jumlah konsonan = ", jumlah_konsonan)
print("Jumlah angka = ", jumlah_angka)