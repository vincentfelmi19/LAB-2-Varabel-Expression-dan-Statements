# Nama: Vincentsius Felmi Ajang
# Universitas Kristen Duta Wacana
'''
Membuat kalkulator sederhana referensi Modul Praktikum 4 (4.4.2) pada contoh 4.2
Buatlah sebuah program kalkulator sederhana yang memiliki fungsi tambah, kurang, kali dan bagi.
Fungsi yang dibuat digunakan untuk mencari hasil dari 2 buah angka sesuai fungsi yang ingin dipilih user.

'''

'''
Input : angka1, angka2, pilih

Proses : tambah(angka1, angka2), kurang(angka1, angka2), kali(angka1, angka2), bagi(angka1, angka2), hasil

Output : hasil

'''
def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    if angka2 == 0:
        print("Syntax Error")
    else:
        return angka1 / angka2

# Input
print("-----SELAMAT DATANG DI PROGRAM KALKULATOR SEDERHANA-----")
print("========================================================")

print("Silahkan pilih fungsi :")
print("1. Tambah\n2. Kurang\n3. Kali\n4. Bagi")
pilih = int(input("Masukkan pilihan anda : "))
angka1 = int(input("Masukkan angka ke-1 = "))
angka2 = int(input("Masukkan angka ke-2 = "))

# Proses
if pilih == 1:
    print("Hasil tambah = ",tambah(angka1,angka2))
elif pilih == 2:
    print("Hasil kurang = ", kurang(angka1,angka2))
elif pilih == 3:
    print("Hasil kali = ", kali(angka1,angka2))
elif pilih == 4:
    print("Hasil bagi = ", bagi(angka1,angka2))
else :
    print("Fungsi yang anda pilih tidak tersedia")