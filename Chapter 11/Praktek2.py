from datetime import *

tglskrng = datetime.date(datetime.now())
tglkembali = tglskrng + timedelta(days=7)
myFile= open('data peminjaman perpus.txt', 'a+')

while True :
    print('')
    kode = input('Masukkan Kode Member	: ')
    nama = input('Masukkan Nama Member	: ')
    judulBuku = input('Masukkan Judul Buku 	: ')

    data = kode + '|' + nama + '|' + judulBuku + '|' + str(tglskrng) + '|' + str(tglkembali) + '\n'
    myFile.write(data)

    print('')
    lanjut = input('Ulangi lagi (y/n)	    : ')
    if lanjut in ('n', 'N'):
        print('')
        print('Terima kasih, data yang anda masukan tekah berhasil diinput.')
        break
myFile.close()