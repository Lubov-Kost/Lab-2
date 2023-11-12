with open('books.csv') as f:
    s = []
    for i in f:
        s.append(i.split(';'))

    #task 1

    k = 0 
    for i in range(1,len(s)):
        if len(s[i][1])>30:
            k+=1
    print(k)

    #task 2 (Реализую поиск по Автору с ФИО)

    zap = input()
    k=0 
    for i in range(1,len(s)):
        if s[i][4]==zap:
            k+=1
            if s[i][6][6:10]=='2014' or s[i][6][6:10]=='2016' or s[i][6][6:10]=='2017':
                print(f'{k}. {s[i][1]}')

    #task 3

    from random import randrange

    kin = [randrange(1,len(s)) for x in range(20)]
    
    for i in range(20):
        kin[i] = f'<{s[kin[i]][3]}>. <{s[kin[i]][1]}> - <{s[kin[i]][6][6:10]}>'

    with open('kin.txt', 'w') as f:
        for num, line in enumerate(kin):
            f.write(f'{num + 1}. {line}\n')