# Nama: Vincentsius Felmi Ajang
# Universitas Kristen Duta Wacana
'''
Pembayaran tagihan referensi Modul Praktikum 6 (6.4) contoh 6.4
Buatlah sebuah program untuk membuat pembayaran tagihan token listrik, air, pulsa, dan WiFi.
Sebelum itu user harus dipastikan memuliki saldo terlebih dahulu dan jika tidak ada saldo pembayaran tidak dapat dilakukan.
Tetapi user bisa melakukan isi saldo / penyetoran untuk mengisi saldo dan program tidak akan berakhir,
kecuali user memilih untuk keluar dari program.

'''

'''
Input : Saldo, Pembayaran(Token Listrik, Air, Pulsa, dan Wifi), Penyetoran(Setor)

Proses : While(Pembayaran(Token Listrik, Air, Pulsa, dan Wifi), Penyetoran) 

Output : Sisa saldo, Pembayaran(Token Listrik, Air, Pulsa, atau Wifi), Sukses / Tidak

'''
# Input
saldo = int(input("Masukkan saldo: "))

# Proses
while(True):
    print("Pilih menu: ")
    print("1. Pembayaran\n2. Penyetoran\n0. Keluar")
    pilihan = int(input("Masukkan pilihan anda: "))
    if pilihan == 1:
        print("Silahkan pilih untuk bayar apa: ")
        print("1. Token Listrik\n2. Air\n3. Pulsa\n4. WiFi\n0. Keluar")
        # Input
        pembayaran = int(input("Masukkan pilihan anda: "))
        if pembayaran == 1:
            tagihan = int(input("Tagihan = "))
            if saldo <= 0:
                print("Saldo kurang, tidak dapat melakukan pembayaran")
            else:
                sisa_saldo = saldo - tagihan
                print("Pembayaran Tagihan Token Listrik Sukses")
                print("Sisa saldo = ",(sisa_saldo))
        elif pembayaran == 2:
            tagihan = int(input("Tagihan = "))
            if saldo <= 0:
                print("Saldo kurang, tidak dapat melakukan pembayaran")
            else:
                sisa_saldo = saldo - tagihan
                print("Pembayaran Tagihan Air Sukses")
                print("Sisa saldo = ",(sisa_saldo))
        elif pembayaran == 3:
            tagihan = int(input("Tagihan = "))
            if saldo <= 0:
                print("Saldo kurang, tidak dapat melakukan pembayaran")
            else:
                sisa_saldo = saldo - tagihan
                print("Pembayaran Tagihan Pulsa Sukses")
                print("Sisa saldo = ",(sisa_saldo))
        elif pembayaran == 4:
            tagihan = int(input("Tagihan = "))
            if saldo <= 0:
                print("Saldo kurang, tidak dapat melakukan pembayaran")
            else:
                sisa_saldo = saldo - tagihan
                print("Pembayaran Tagihan WiFi Sukses")
                print("Sisa saldo = ",(sisa_saldo))
        elif pembayaran == 0:
            break 
    elif pilihan == 2:
        isi_saldo = int(input("Masukkan nominal: "))
        saldo = isi_saldo+saldo
        if isi_saldo <= 0:
            print("Penyetoran gagal")
        else:
            print("Saldo berhasil diisi")
    elif pilihan == 0:
        break