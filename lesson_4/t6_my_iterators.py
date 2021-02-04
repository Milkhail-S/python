from itertools import count
from itertools import cycle


# итератор 10 значений от точки отсчёта
start = int(input('Введите точку отсчёта в виде целого числа: '))
for i in count(start):
    if i > start + 10:
        break
    print(i)

# итератор перебора
lst = ['start', 1, 2, 3, 'end']
sch = 0
for i in cycle(lst):
    if sch > 8:
        break
    sch += 1
    print(i)


