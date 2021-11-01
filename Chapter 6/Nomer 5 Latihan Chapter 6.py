def sum(*bil):
    hasil = 0
    for i in bil:
        hasil += i
    print(hasil)

def average(*bil):
    sum = 0
    i = 1
    for i in bil:
        sum += i
        i += 1
    hasil = sum / i
    print(hasil)

def maks(*bil):
    hasil = 0
    for i in bil:
        if i >= hasil:
            hasil = i
    print(hasil)

def min(*bil):
    hasil = 99999999999
    for i in bil:
        if i <= hasil:
            hasil = i
    print(hasil)

print('Total dari seluruh nilai bilangan : ')
sum(5, 10, 4, 9, 30, 16, 2, 11)
print('Rata-rata : ')
average(5, 10, 4, 9, 30, 16, 2, 11)
print('Nilai Maksimum : ')
maks(5, 10, 4, 9, 30, 16, 2, 11)
print('Nilai Minimum : ')
min(5, 10, 4, 9, 30, 16, 2, 11)

print('')
print('Total dari seluruh nilai bilangan : ')
sum(81, 98, 12, 83, 45, 77, 69, 30, 56)
print('Rata-rata : ')
average(81, 98, 12, 83, 45, 77, 69, 30, 56)
print('Nilai Maksimum : ')
maks(81, 98, 12, 83, 45, 77, 69, 30, 56)
print('Nilai Minimum : ')
min(81, 98, 12, 83, 45, 77, 69, 30, 56)
