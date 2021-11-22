Daftarsayur = ['bayam', 'kangkung', 'wortel', 'selada']

def menambahdata():
    tambahsayur = input('Masukkan sayur yang ingin ditambahkan : ')
    Daftarsayur.append(tambahsayur)

def menghapusdata():
    try:
        Hapussayur = input('Masukkan sayur yang ingin dihapus : ')
        Daftarsayur.remove (Hapussayur)
    except ValueError:
        print('Data tidak ditemukan didata nih')


def menampilkandata():
    for x in range(len(Daftarsayur)):
        print(Daftarsayur[x])

while True:
    print('Menu')
    print('A.Tambah data sayur')
    print('B.Hapus data sayur')
    print('C.Tampilkan data sayur')
    option = input('Silahkan Pilih Yaw : ')
    if option == 'A' :
        menambahdata()
    if option == 'B' :
        menghapusdata()
    if option == 'C' :
        menampilkandata()
        break


