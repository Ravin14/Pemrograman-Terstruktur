KodeStaff = input("Masukkan Kode Karyawan: ")
NamaStaff = input("Masukkan Nama Karyawan: ")
GolonganStaff = str(input("Masukkan Golongan     : "))
if (GolonganStaff == "A") or (GolonganStaff == "a"):
    GajiPokok = 10000000
    Persen = 2.5

elif (GolonganStaff == "B") or (GolonganStaff == "b"):
    GajiPokok = 8500000
    Persen = 2.0

elif (GolonganStaff == "C") or (GolonganStaff == "c"):
    GajiPokok = 7000000
    Persen = 1.5

elif (GolonganStaff == "D") or (GolonganStaff == "d"):
    GajiPokok = 5500000
    Persen = 1.0

else:
    print("Golongan tidak valid")

GajiKotor = Persen / 100 * GajiPokok
GajiBersih = GajiPokok - GajiKotor

print("||||||||||||||||||||||||||||||||||")
print("STRUK RINCIAN GAJI KARYAWAN")
print("***********************************")
print("Nama Karyawan    : " + NamaStaff + " (Kode : " + KodeStaff + ")")
print("Golongan         : " + GolonganStaff)
print("***********************************")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Potongan (" + str(Persen) + "%)  : Rp.", int(GajiKotor))
print("************************************")
print("Gaji Bersih      : Rp.", int(GajiBersih))