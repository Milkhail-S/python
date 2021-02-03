def div_func():
    p1 = float(input('Ввведите делимое: '))
    p2 = float(input('Введите делитель: '))
    try:
        res = p1 / p2
    except ZeroDivisionError as err:
        print(err)
        return
    return res


print(f'Частное: {div_func()}')
