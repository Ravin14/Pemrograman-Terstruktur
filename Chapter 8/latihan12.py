buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
while True:
    print('=====Menu=====')
    print('a. Tambah data buah')
    print('b. Beli buah')
    print('c. Beli buah')
    pilihan = input('Pilihan menu : ')
    print('')

    if pilihan == 'A' or pilihan == 'a':
        print('Tambah Data Buah')
        menambah = input('Masukkan nama buah: ')
        if menambah in buah:
            print('Ini buah udah ada ya sayangg:)')
        else:
            daftarharga = int(input('Harga buah: '))
            buah[menambah] = daftarharga
            print('Data buah: ')
            for x, y in buah.items():
                print('-', x, '(Harganya Rp.' + str(y) + ')')
            print('')
            True
    elif pilihan == 'B' or pilihan == 'b':
        print('-Hapus Data Buah-')
        menghapus = input('Masukkan nama buahnya yaw : ')
        if menghapus in buah:
            del buah[menghapus]
            True
        else:
            print('Nama buah tidak ndak ditemukan')

    elif pilihan == 'C' or pilihan == 'c':
        print('-Pilihan Buah-')
        print(buah)
        totalharga = 0
        try:
            while True:
                beli = input('Buah yang akan dibeli: ')
                if beli in buah:
                    banyakkg = int(input('Berapa Kg       : '))
                    cek = input('Mau beli yang lain gak(y/n)? ')
                    total = banyakkg * buah[beli]
                    totalharga += total
                    if cek == 'Y' or cek == 'y':
                        True
                    elif cek == 'N' or cek == 'n':
                        print('----------------------------')
                        print('Total harga     :', totalharga)
                        print('')
                        break
                    else:
                        print('Yang kamu cari gak ada nih, pilih yang lain yaw!!')
                        break
                else:
                    print('Yahhh buah tidak tersedia')
        except ValueError:
            print('input tidak valid')

    else:
        print('Pilihan tidak tersedia')

