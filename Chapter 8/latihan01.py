try:
    banyak = int(input('Mau masukin berapa bilangan kawan ? : '))
    bill = []

    for i in range(banyak):
        inputangka = int(input('Masukkan bilangan bulat : '))
        bill = [inputangka] + bill

    bill.sort(reverse=True)
    print('Ini semua bilangan yang kamu masukin : ', bill)

except ValueError:
    print('HUH, YANG KAMU MASUKIN BUKAN BILANGAN!!!')

