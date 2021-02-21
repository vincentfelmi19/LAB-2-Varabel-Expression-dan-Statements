# Nama: Vincentsius Felmi Ajang
# Universitas Kristen Duta Wacana
'''
Mencari nilai terkecil referensi Modul Praktikum 3 (3.4.1) pada contoh 3.3
Buatlah sebuah program yang meminta lima input bilangan kemudian mencari 
nilai terkecil dari kelima bilangan tersebut.
catatan : user yang memberikan inputan

'''

'''
Input : minimal, bilangan1, bilangan2, bilangan3, bilangan4, bilangan5

Proses : minimal, if{ minimal > bilangan1, minimal > bilangan2, minimal > bilangan3, minimal > bilangan4, minimal > bilangan5 }

Output : minimal

'''

# Input
minimal = 999_999

bilangan1 = int(input("Masukkan bilangan ke-1 = "))
bilangan2 = int(input("Masukkan bilangan ke-2 = "))
bilangan3 = int(input("Masukkan bilangan ke-3 = "))
bilangan4 = int(input("Masukkan bilangan ke-4 = "))
bilangan5 = int(input("Masukkan bilangan ke-5 = "))

# Proses
if minimal > bilangan1 :
    minimal = bilangan1
if minimal > bilangan2 :
    minimal = bilangan2
if minimal > bilangan3 :
    minimal = bilangan3
if minimal > bilangan4 :
    minimal = bilangan4
if minimal > bilangan5 :
    minimal = bilangan5

# Output
print("Nilai terkecil dari ke-5 bilangan adalah : ",minimal)