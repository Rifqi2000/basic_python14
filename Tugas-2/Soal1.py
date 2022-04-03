kontak = [["Rifqi", "082133172777"]]
while True:
    print("--Menu--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    pilih = int(input("Pilih menu: "))

    if pilih == 1:
        for i in range(len(kontak)):
            print("Nama\t\t: ", kontak[i][0])
            print("No Telepon\t: ", kontak[i][1])
    elif pilih == 2:
        tambah_kontak = []
        nama = input("Nama\t\t: ")
        nomor = input("No Telepon\t: ")
        tambah_kontak.append(nama)
        tambah_kontak.append(nomor)
        kontak.append(tambah_kontak)
    elif pilih == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia")
