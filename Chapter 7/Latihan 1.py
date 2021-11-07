inputFile=input('Masukkan nama file yang dicari : ')

try:
    file=open(inputFile, "r")
    print('Isi file dari', inputFile, 'adalah: ', file.read())
except FileNotFoundError:
    print('File tidak ditemukan atau terdapat salah dalam penulisan')


