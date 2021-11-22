buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
while True:
    print('=====Menu=====')
    print('a. Tambah data buah')
    print('b. Beli buah')
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
        print('Pilihan Buah')
        print(buah)
        totalharga = 0
        while True:
                beli = input('Nama buah yang dibeli : ')
                if beli in buah:
                        banyakkg = int(input('Berapa Kilogram   : '))
                        cek = input('Mau beli yang lain gak (yes or no) ? ')
                        total = banyakkg * buah[beli]
                        totalharga += total
                        if cek == 'Yes' or cek == 'yes':
                                True
                        elif cek == 'No' or cek == 'no':
                                print('*************************')
                                print('Total harga     :', totalharga)
                                break
                        else:
                                print('Yang kamu cari gak ada nih, pilih yang lain yaw!!')
                                break
                else:
                        print('Yang kamu cari gak ada nih kayak perasaan dia ke aku:) Cari yang bener yaw!!')