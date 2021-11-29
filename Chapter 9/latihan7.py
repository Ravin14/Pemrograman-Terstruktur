mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print('===========================================================================')
print('NIM      NAMA MAHASISWA          TGL LAHIR          TEMPAT LAHIR')
print('---------------------------------------------------------------------------')

x = 0
for isi in mhs:
    data = mhs[x].split(':')
    nim = data[0]
    nama = data[1]
    tanggal = data[2].split('-')
    tanggal = tanggal[2] +'/'+ tanggal[1] +'/'+ tanggal[0]
    tempat = data[3]
    x += 1
    print(nim.ljust(9), end='')
    print(nama.ljust(24), end='')
    print(tanggal.ljust(19), end='')
    print(tempat.ljust(12))

print('---------------------------------------------------------------------------')