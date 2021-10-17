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

StatusMenikah = int(input("Pilih Status (1: Menikah, 2: Belum) : "))

if (StatusMenikah == 1):
    Status = "Menikah"
    TunjanganMenikah = 10 / 100 * GajiPokok
    JumlahAnak = int(input("Berapa jumlah Anak  : "))
    TunjanganAnak = 5 / 100 * GajiPokok
    TunjanganAnak = TunjanganAnak * JumlahAnak

elif (StatusMenikah == 2):
    Status = "Belum Menikah"
    TunjanganMenikah = 0
    TunjanganAnak = 0
    JumlahAnak = "-"

else:
    print("Status Menikah Tidak Valid")

GajiKotor = GajiPokok + TunjanganMenikah + TunjanganAnak
potongan = Persen / 100 * GajiKotor
GajiBersih = GajiKotor - potongan

GajiKotor = Persen / 100 * GajiPokok
GajiBersih = GajiPokok - GajiKotor

print("|||||||||||||||||||||||||||||||||||||")
print("STRUK RINCIAN GAJI KARYAWAN")
print("*************************************")
print("Nama Karyawan    : " + NamaStaff + " (Kode : " + KodeStaff + ")")
print("Golongan         : " + GolonganStaff)
print("Status Menikah   : " + Status)
print("Jumlah Anak      : " + str(JumlahAnak))
print("*************************************")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Tunjangan Menikah: Rp.", int(TunjanganMenikah))
print("Tunjangan Anak   : Rp.", int(TunjanganAnak))
print("*************************************")
print("Gaji Kotor       : Rp.", int(GajiKotor))
print("Potongan (" + str(Persen) + "%)  : Rp.", int(Persen))
print("*************************************")
print("Gaji Bersih      : Rp.", int(GajiBersih))
print("*************************************")
print("||||||||||||||||||||||||||||||||||")
print("STRUK RINCIAN GAJI KARYAWAN")
print("*************************************")
print("Nama Karyawan    : " + NamaStaff + " (Kode : " + KodeStaff + ")")
print("Golongan         : " + GolonganStaff)
print("*************************************")
print("Gaji Pokok       : Rp.", GajiPokok)
print("Potongan (" + str(Persen) + "%)  : Rp.", int(GajiKotor))
print("*************************************")
print("Gaji Bersih      : Rp.", int(GajiBersih))