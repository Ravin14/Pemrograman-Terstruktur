from datetime import *

tglskrng = datetime.date(datetime.now())
myFile = open('data peminjaman perpus.txt', 'r')

print('')
carikode = input('Masukkan Kode Member yaw        :  ')

kode= []
nama = []
jdlbk = []
tglpnjm = []
tglhrskmbl = []

for isi in myFile:
    pecah = isi.split('|')
    kode += [pecah[0]]
    nama += [pecah[1]]
    jdlbk += [pecah[2]]
    tglpnjm += [pecah[3]]
    tglhrskmbl += [pecah[4]]

if carikode in kode:
    x = kode.index(carikode)
    print('')
    print('Data Peminjaman Buku')
    print('Kode 	        	    : ', kode[x])
    print('Nama 		            : ', nama[x])
    print('Judul  		            : ', jdlbk[x])
    print('Tanggal Mulai Peminjaman	: ', tglpnjm[x])
    print('Tanggal Maks Peminjaman   : ', tglhrskmbl[x].replace('\n', ''))
    print('Tanggal Pengembalian	    : ', str(tglskrng))

    minjam = tglpnjm[x].split('-')
    for item in minjam:
        thnpinjam = minjam[0]
        blnpinjam = minjam[1]
        tglpinjam = minjam[2]

    slisih = tglskrng - date(int(thnpinjam), int(blnpinjam), int(tglpinjam))
    slisihHari = slisih.days
    if slisihHari >= 7:
        telat = slisihHari - 7
    else:
        telat = 0

    print('Terlambat                       : ', telat, ' hari')
    print('Denda			        :  Rp ', telat * 2000)

else:
    print('')
    print('Data peminjaman yang dicari tidak ada')