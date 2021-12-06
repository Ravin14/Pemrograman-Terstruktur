myfile = open('praktek1.txt', 'r')
isi = myfile.readlines()

genap = 0
ganjil = 0
for i in range (len(isi)) :
    if int(isi[i]) % 2 == 0 :
        genap += 1
    else:
        ganjil += 1

myfile.close()

print('Jumlah Bilangan Ganjil :', ganjil)
print('Jumlah Bilangan Genap  :', genap)