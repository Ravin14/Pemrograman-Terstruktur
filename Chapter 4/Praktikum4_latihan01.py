#tarif
tarifawal = 200000#12jam
tarifselanjutnya = 10000#per-jam
#waktu
awalwakturental = 06.00
akhirwakturental = 23.50
#menghitung berapa lama rental
lamarental = int(akhirwakturental-awalwakturental)
#menghitung waktu rental setelah 12 jam
lamarentalselanjutnya = lamarental-12
#mengihuting biaya yang dikeluarkan
tarifsetelahrental12jam = lamarentalselanjutnya * tarifselanjutnya
totalbiaya = tarifawal+tarifsetelahrental12jam
print(totalbiaya)