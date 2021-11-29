import random
def shuffleString(x, n):
    j = []
    x = list(x)
    i = 0
    while i < n :
        random.shuffle(x)
        acak = ''.join(x)
        i += 1
        if acak not in j:
            j.append(acak)
        else :
            i -= 1
    print(j)

shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
shuffleString('aku', 5)