def harga(x):
    Maksimal = max(x.values())
    for x,y in x.items():
        if y == Maksimal:
            return x
buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
print(buah)
print('Buah paling mahal:',harga(buah))