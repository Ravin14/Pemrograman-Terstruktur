daftar = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
          {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
          {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
          {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
          {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

x = 0
for data in daftar :
    mhs = daftar[x]
    nim = mhs['nim']
    nama = mhs['nama']
    mid = str(mhs['mid'])
    uas = str(mhs['uas'])
    nilaiAkhir = round((mhs['mid'] + 2*mhs['uas'])/3)
    status = ''
    if nilaiAkhir >= 60 :
        status = 'LULUS'
    else:
        status = 'TIDAK LULUS'

print('================================================================')
print('NIM    NAMA         N.MID     N.UAS      N.AKHIR       STATUS')
print('----------------------------------------------------------------')

for x in range(len(daftar)) :
    print(daftar[x]['nim'].ljust(7), end='')
    print(daftar[x]['nama'].ljust(10), end='')
    print(str(daftar[x]['mid']).rjust(8), end='')
    print(str(daftar[x]['uas']).rjust(10), end='')
    print(str(nilaiAkhir).rjust(13), end='')
    print(status.rjust(13))

print('================================================================')

