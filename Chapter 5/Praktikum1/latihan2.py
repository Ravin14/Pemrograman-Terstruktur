print("CEK KELULUSAN MAHASISWA")
Name= (input("Name : "))
BahasaIndonesia = int(input("Score Bahasa Indonesia :"))
IPA= int(input("Score IPA :"))
Matematika= int(input("Score Matematika : "))
if(Matematika<0) or (BahasaIndonesia<0) or (IPA<0) or (Matematika>100) or (BahasaIndonesia>100) or (IPA>100):
    print("Input Anda Tidak Valid")
elif(Matematika>70) and (BahasaIndonesia>=60) and (IPA>=60):
    print("Status Kelulusan : ", Name,"Dinyatakan LULUS")
else:
    print("Status Kelulusan : ", Name,"Dinyatakan TIDAK LULUS")
