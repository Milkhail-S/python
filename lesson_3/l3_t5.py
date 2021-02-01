def inf_sum():
    res = []
    while True:
        lst = input('Введите несколько чисел через пробел: ').split()
        for i in lst:
            if i != 'q':
                res.append(int(i))
            else:
                return f'{sum(res)}'
        ito = sum(res)
        print(ito)
    return lst


print(inf_sum())
