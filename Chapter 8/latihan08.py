def rerata(x):
    rata2 = sum(x.values())/len(x)
    return rata2
buah = {'Apel' : 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500}
print('Harga rata2 buah:',rerata(buah))