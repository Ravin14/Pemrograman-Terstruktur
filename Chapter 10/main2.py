myFile = open("datamhs.txt", "r")
cari = input("Masukkan Nim yang ingin di cari :")

nim =[]
nama = []
alamat= []

for data in myFile:
    pecahData = data.split('|')
    nim += [pecahData[0]]
    nama += [pecahData[1]]
    alamat += [pecahData[2]]

    if nim == cari:
        print("Data Mahasiswa")
        print("NIM               :", pecahData[0])
        print("Nama              :", pecahData[1])
        print("Tinggi Badan      :", pecahData[2])
    else:
        print("Data Mahasiswa tidak ditemukan")