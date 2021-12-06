myFile = open('datamhs.txt', 'a+')

while True:
    nim = input('Masukkan NIM		: ')
    nama = input('Masukkan Nama Mhs	: ')
    alamat = input('Masukkan Alamat     : ')
    isi = nim + '|' + nama + '|' + alamat + '\n'
    myFile.write(isi)

    print('')
    lanjut = input('Ulangi input lagi (y/n) : ')
    if lanjut in ("n", "N"):
        break

myFile.close()