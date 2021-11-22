print('---------------------------------------')
print('---------MENGHITUNG HARGA BUAH---------')
print('---------------------------------------')

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(buah)
totalharga = 0
while True:
        beli = input('Nama buah yang dibeli : ')
        if beli in buah:
                banyakkg = int(input('Berapa Kilogram   : '))
                cek = input('Mau beli yang lain gak (yes or no) ? ')
                total = banyakkg * buah[beli]
                totalharga += total
                if cek == 'Yes' or cek == 'yes':
                        True
                elif cek == 'No' or cek == 'no':
                        print('*************************')
                        print('Total harga     :', totalharga)
                        break
                else:
                        print('Yang kamu cari gak ada nih, pilih yang lain yaw!!')
                        break
        else:
                print('Yang kamu cari gak ada nih kayak perasaan dia ke aku:) Cari yang bener yaw!!')