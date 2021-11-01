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