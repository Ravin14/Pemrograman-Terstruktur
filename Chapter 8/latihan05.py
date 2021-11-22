bill = [2, 3, 5, 7, 10]
def kuadrat(bill):
    x = []
    for data in bill:
        data = data ** 2
        x = x + [data]
    return x

print(kuadrat(bill))




