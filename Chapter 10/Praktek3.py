try:
    myFile = open('datamhs.txt', 'r')
    list = []
    baca = myFile.readlines()

    for i in range(len(baca)):
        split = baca[i].split('|')
        dataDict = {'nim': split[0], 'nama': split[1], 'alamat': split[2].replace('\n', '')}
        list += [dataDict]

    print('dataMhs = ', list)
    myFile.close()

except FileNotFoundError:
    print("Yah file yang kamu cari tidak ditemukan nich")
