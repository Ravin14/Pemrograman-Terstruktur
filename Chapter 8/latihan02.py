def datastat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    return(a,b,c)

data = []
Total = int(input('Mau masukin berapa bilangan kawan ? : '))
for i in range(Total):
    inputangka = int(input('Masukkan angka yukkk : '))
    data.append(inputangka)
print('Rerata,Max,Min:',datastat(data))