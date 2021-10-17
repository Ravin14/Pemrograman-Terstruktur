from random import randint
Angka = randint(0, 100)
Nilai = 100
print ('Anyeong.. Kenalin namaku Mr. Ius , Aku udah milih sebuah bilangan bulat secara acak antara 0 sampai dengan 100 lur. Buruan tebak dan dapatkan  hadiah iphone 13!!')
while True:
    menebak = int(input('Tebakanmu : '))
    if menebak > Angka :
        print ('HAHAHAHA Bilanganmu masih kegedean:)')
    elif menebak < Angka :
        print ('AWOWKWKWK Bilanganmu kok kecil banget sih')
    elif menebak == Angka :
        print ('Perfecto!! Kamu seorang jenius karna tebakanmu benar, Selamat ya:D pajak ditanggung pemenang:)))')
        break
    Nilai -= 2
    if Nilai == 0:
        print('FUFUFU nilai kamu kok udah 0 aja, yah sayang sekali ga bisa lanjut nebak lagi:) Tetap menyerah jangan semangat!!!')
print('Kukasih tau nilaimu nih say :', Nilai)