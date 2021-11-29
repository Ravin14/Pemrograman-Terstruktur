def star2(n) :
    for x in range(int(n/2)) :
        print(('*'*(x*2+1)).center(n*2-1))
    for x in reversed (range(int(n/2+1))) :
        print(('*'*(x*2+1)).center(n*2-1))

star2(7)




