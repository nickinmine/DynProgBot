def backpack(c, a, y):
    c = [0] + c
    a = [0] + a
    f = [[]] * (len(c))
    for k in range(0, len(c)):
        f[k] = [0] * (y + 1)

    for k in range(1, len(c)):
        for i in range(1, y + 1):
            if k == 1:
                f[k][i] = i // a[k] * c[k]
            elif (i - a[k]) >= 0:
                f[k][i] = max(f[k - 1][i], f[k][i - a[k]] + c[k])
            else:
                f[k][i] = f[k - 1][i]

    for k in range(1, len(c)):
        for i in range(1, y + 1):
            print(f[k][i], end='\t')
        print("\n", end='')

    x = [0] * len(c)
    k = len(c) - 1
    i = y
    while k > 0 and i > 0:
        if f[k][i] == f[k-1][i]:
            k -= 1
        else:
            x[k] += 1
            i -= a[k]

    for i in range(1, len(x)):
        print(x[i], end=' ')
    print()
    f.append(x)
    return f


if __name__ == '__main__':
    c = [8, 5, 1]
    a = [3, 2, 1]
    y = 13
    backpack(c, a, y)
