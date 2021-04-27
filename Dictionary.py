# Nama: Vincentsius Felmi Ajang
# Universitas Kristen Duta Wacana
'''
Membuat program Dictionary, Referensi Modul praktikum 10 (10.3.1).
Buatlah sebuah program untuk memisahkan huruf konsonan dan vokal dari sebuah kata
yang diinputkan oleh user, kedalam 2 buah Dictionary berbeda dan 
hitunglah berapa jumlah huruf itu sebagai value.

'''

'''
Input : kata, huruf_konsonan, huruf_vokal, dict_konsonan, dict_vokal

Proses : for(huruf in kata), dict_konsonan, dict_vokal, if huruf in huruf_konsonan , if huruf in huruf_vokal , 
         if huruf not in dict_konsonan => dict_konsonan[huruf] = 1, else dict_konsonan[huruf] += 1
         if huruf not in dict_vokal => dict_vokal[huruf] = 1, else dict_vokal[huruf] += 1

Output : dict_konsonan, dict_vokal

'''

# Input
kata = input("Masukkan kata: ")
huruf_konsonan = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
huruf_vokal = "AIUEOaiueo"
dict_konsonan = dict()
dict_vokal = dict()

# Proses
for huruf in kata:
    if huruf in huruf_konsonan:
        if huruf not in dict_konsonan:
            dict_konsonan[huruf] = 1
        else:
            dict_konsonan[huruf] += 1
    if huruf in huruf_vokal:
        if huruf not in dict_vokal:
            dict_vokal[huruf] = 1
        else:
            dict_vokal[huruf] += 1

# Output
print(dict_vokal)
print(dict_konsonan)