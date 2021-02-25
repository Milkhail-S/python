class ZeroDivisionOops(Exception):
    def __init__(self, text='Деление на ноль недопустимо, но простительно.'):
        print(text)


chi = int(input('Введите числитель: '))
zna = int(input('Введите знаменатель: '))
try:
    chi / zna
except ZeroDivisionError:
    print(0)
    try:
        if zna == 0:
            raise ZeroDivisionOops()
    except ZeroDivisionOops:
        pass
    pass
