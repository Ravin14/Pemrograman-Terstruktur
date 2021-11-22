print('---------------------------------------')
print('---------MENGHITUNG HARGA BUAH---------')
print('---------------------------------------')

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
beli = input('Nama buah yang dibeli: ')
if beli in buah:
    try:
        banyakkg = int(input('Berapa Kilogram        : '))
        hasil = banyakkg * buah[beli]
        print('----------------------')
        print('Total harga     :',hasil)
    except ValueError:
        print('Yuk tolong banget masukin yang bener yaw')
else:
    print('Yah buahnya gak ditemukan:3 ')