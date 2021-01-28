chi = int(input('Введите целое положительное число: '))
n = 0
ls = []
bit = []
while chi > 0:
    cif = chi % 10
    chi = chi // 10
    ls.insert(n, cif)
    n += 1
wow = max(ls)
print(f'Максимальная цифра во введённом числе: {wow}')

