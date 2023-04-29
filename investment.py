def investment(f, c):
    print('Условие задачи')
    print('f[1]', 'f[2]', 'f[3]', sep='\t')
    for k in range(0, len(f)):
        for i in range(0, len(f[k])):
            print(f[k][i], end='\t')
        print("\n", end='')
    print("\n", end='')

    s = [[]] * (len(f))
    for k in range(0, len(f)):
        s[k] = [0] * len(f[k])
    for k in range(0, len(f)):
        s[k][2] = f[k][2]

    temp = [0] * len(f[0])
    step = [0] * len(f[0])

    for n in range(len(f[0]), 0, -1):
        print('Шаг: t=', n, sep='')
        if (n == len(f[0])):
            print('x', 'u', 's[3,x]', sep='\t')
            for k in range(0, len(s)):
                for i in range(0, len(s[k])):
                    print(s[k][i], end='\t')
                print("\n", end='')
        else:
            print('x', 'u', 'x-u', 'f[2,u]', 's[3,x-u', 'sum', 'max', sep='\t')
            for x in range(0, c + 1):
                for u in range(0, x + 1):                    
                    sm = round(f[u][n - 1] + s[x-u][n], 2)
                    if (sm > temp[n - 1]):
                        step[n - 1] = u
                    temp[n - 1] = max(temp[n - 1], sm)
                    print(x, u, x-u, f[u][n - 1], s[x-u][n], sm, temp[n - 1], sep= '\t')
                    s[x][n - 1] = temp[n - 1]
        print("\n", end='')
        
    print('Ответ')
    print(temp[len(temp) - 2])
    
    print('Восстановление ответа')
    print('f[1]', 'f[2]', 'f[3]', sep='\t')
    sm = 0
    for i in range(len(step) - 1):
        sm += step[i]
    step[len(step) - 1] = c - sm
    for i in range(len(step)):
        print(step[i], end='\t')
    
    return f


t = [[0, 0, 0],
     [3.22, 3.33, 4.27],
     [3.57, 4.87, 7.64],
     [4.12, 5.26, 10.25],
     [4, 7.34, 15.93],
     [4.85, 9.49, 16.12]]
c = 5

f = investment(t, c)
