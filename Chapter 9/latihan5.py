daftar = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
          {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
          {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
          {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
          {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('==================================================')
print('NIM      NAMA       N.MID     N.UAS')
print('--------------------------------------------------')

for x in range(len(daftar)) :
    print(daftar[x]['nim'].ljust(7), end='')
    print(daftar[x]['nama'].ljust(10), end='')
    print(str(daftar[x]['mid']).rjust(8), end='')
    print(str(daftar[x]['uas']).rjust(10))

print('==================================================')

