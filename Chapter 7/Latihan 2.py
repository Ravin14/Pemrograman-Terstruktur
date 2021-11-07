fileInput = input(' Input nama file : ')
lagi = 'y'

try:
    file = open(fileInput, "r")
    while lagi == 'y':
        Baca = input('Data yang akan ditambah nich : ')
        file = open(fileInput, "a")
        file.write(Baca)
        lagi = input('Lagi ndak nich (y/n): ')
        file = open(fileInput, "a")
        file.close()

except FileNotFoundError:
    print('Filenya ndak ditemukan nich atau ada kesalahan penulisan yaw')
