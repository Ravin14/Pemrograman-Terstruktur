data = []
Berapa = int(input('Mau berapa mahasiswa nih yang diinput ? '))
for i in range(Berapa):
    user = input( 'Masukin namanya yaw : ')
    data.append(user)

for user in data:
    print(user, '(' + str(len(user)) + ' karakter)')