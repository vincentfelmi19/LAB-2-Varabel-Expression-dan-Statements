# Nama: Vincentsius Felmi Ajang
# Universitas Kristen Duta Wacana

'''
Mengecek palindrom referensi Modul Praktikum 11 (11.4) pada contoh kasus 11.1
Buatlah sebuah program yang dapat mengecek apakah kata yang diinputkan oleh user,
adalah kata yang bersifat palindrom atau tidak, dengan menggunakan tuple.

'''

'''
Input : kata_user

Proses : def palindrom, balik_kata, if kata_user == balik_kata, else

Output : kata_user, balik_kata, palindrom / tidak

'''

# Proses
def palindrom(kata_user):
    balik_kata = kata_user[::-1]
    print(type(balik_kata),type(kata_user))
    
    # Output1
    print("Kata yang diberikan: ",kata_user)
    # Output2
    print("Kata yang dibalik: ", balik_kata)

    if kata_user == balik_kata:
        # Output3a
        print("Kata yang diberikan bersifat palindrom")
    else:
        # Output3b
        print("Kata tidak bersifat palindrom")

# Input
kata_user = tuple(input("Masukkan kata: "))
palindrom(kata_user)