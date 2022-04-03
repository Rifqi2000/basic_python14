nama_kontak = ['Farhan', 'Joko']
nomor_telepon = ["08123456789","08987654321"]

def daftar_kontak():
    for i in range(len(nama_kontak)):
        print("Nama\t\t: ", nama_kontak[i])
        print("No Telepon\t: ", nomor_telepon[i])

def tambah_kontak():
    nama = input("Nama\t\t: ")
    nomor = input("No Telepon\t: ")
    nama_kontak.append(nama)
    nomor_telepon.append(nomor)

while True:
    print("--Menu--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    pilih = int(input("Pilih menu: "))

    if pilih == 1:
        daftar_kontak()
    elif pilih == 2:
        tambah_kontak()
    elif pilih == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")

