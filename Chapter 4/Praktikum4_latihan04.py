import math
jarakAB = 125
kecepatanAB = 62
waktuAB = int(jarakAB/kecepatanAB)*60
istirahatB = 45
jarakBC = 256
kecepatanBC = 70
waktuBC = int(jarakBC/kecepatanBC)*60
totalwaktumenit = waktuAB+istirahatB+waktuBC #3454
totalwaktujamdesimal = totalwaktumenit/60 #5.75
waktubelakang = math.floor((6+totalwaktujamdesimal) % 1 / 0.25*15) #45
totalwaktujam = math.floor(totalwaktumenit/60) + waktubelakang/100 #45/100
waktudepan = math.floor(6+totalwaktujamdesimal) #11
print("waktu yang dibutuhkan dalam menit = " + str(totalwaktumenit))
print("waktu yang dibutuhkan dalam jam = " + str(totalwaktujam))
print("perkiraan waktu Pak amir sampai = " + str(waktudepan) + '.' + str(waktubelakang))