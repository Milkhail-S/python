rev = int(input('Введите сумму выручки: '))
cost = int(input ('Введите сумму издержек: '))
if cost > rev:
    print('Издержки больше выручки')
elif cost < rev:
    print('Выручка больше издержек')
    prof = (rev-cost)/rev
    pr = rev - cost
    print(f'Прибыль компании составила: {prof:.2%}')
    emp = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на сотрудника составила: {pr/emp:.2f}')
elif cost == rev:
    print('Работаем в 0, нужны идеи!')
