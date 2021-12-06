file = input('Masukkan nama file : ')
keyword = int(input('Masukkan nilai n : '))
myfile = open (file, 'r')
baca = myfile.read()

list =[]
for i in baca :
    if i.isalpha() :
        shift = ord(i)
        shift += keyword
        if (shift > ord('Z')) :
            shift -= 26
        akhir = chr(shift)
    elif i.isspace() :
        akhir = chr(32)
    list += [akhir]

newfile = open('hasil dari penyandian nomer 6.txt', 'w')
newfile.write(''.join(list))
myfile.close()
newfile.close()