from random import randint
Angka = randint(0, 100)
print ('Anyeong.. Kenalin namaku Mr. Ius , Aku udah milih sebuah bilangan bulat secara acak antara 0 sampai dengan 100 lur. Buruan tebak dan dapatkan  hadiah iphone 13!!')
while True:
    menebak = int(input('Tebakanmu : '))
    if menebak > Angka :
        print ('HAHAHAHA Bilanganmu masih kegedean:)')
    elif menebak < Angka :
        print ('AWOWKWKWK Bilanganmu kok kecil banget sih')
    elif menebak == Angka :
        print ('Kamu seorang jenius karna tebakanmu benar, Selamat ya:D pajak ditanggung pemenang:)))')
        break