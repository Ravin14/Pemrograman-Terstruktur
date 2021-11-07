print('##################################')
print('PROGRAM UNTUK MENGHITUNG RATA-RATA')
print('##################################')

jumlah = 0
rata = 0
BilanganBenar =  True
while BilanganBenar :
   try:
        masuk = int(input('Input bilangan bulat: '))
        jumlah += masuk
        rata += 1
        ulang = input('Coba lagi ndak nich (y/n)? : ')
        if ulang == "y" :
            BilanganBenar = True
        else :
            BilanganBenar = False
   except ValueError :
        print("Bukan bilangan bulat")
print('\nRata-ratanya yaitu : ', jumlah/rata)
