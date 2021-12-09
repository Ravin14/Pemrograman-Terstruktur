try:
    from datetime import *

    def diffDate(x):
        tanggal1 = datetime.date(datetime.now())
        selisih = abs(x - tanggal1)
        print('Selisih jumlah hari antara tanggal ', tanggal1, ' dan ', x, ' adalah ', selisih.days, ' hari.')

    x = date(2003, 7, 23)
    diffDate(x)
except ValueError:
    print('Yah inputnya gak valid nih')