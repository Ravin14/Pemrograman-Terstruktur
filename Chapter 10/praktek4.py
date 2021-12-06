myfile = open('datamhs.txt', 'r')
nim = []
nama = []
alamat = []

cari = input('Masukkan NIM yang mau dicari : ')

for i in myfile:
    pecah = i.split('|')
    nim += [pecah[0]]
    nama += [pecah[1]]
    alamat += [pecah[2]]

if cari in nim:
    index = nim.index(cari)
    print('')
    print('Data Mahasiswa')
    print('NIM      : ', nim[index])
    print('Nama     : ', nama[index])
    print('Alamat   : ', alamat[index])
