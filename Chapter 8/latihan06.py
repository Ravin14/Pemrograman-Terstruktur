data = ['coklat', 'taro', 'kentang', 'keju']

def sortStringByChar(x):
    data = []
    for i in x:
        menghitung = len(i)
        data.append(menghitung)
        x.sort(reverse=True)
    return x
print(sortStringByChar(data))