items = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})
]


while True:
    inf = input('Для выхода введите "q", для продолжения - любой другой символ: ')
    if inf != 'q':
        art, name, price, qty, uom = input('Введите через пробел артикул, название, цену, количество и единицу измерения товара: ').split()
        items.append((art, {
            'название': name,
            'цена': float(price),
            'количество': int(qty),
            'ед': uom,
        }))
    else:
        break
# keys = []
res = {
    'название': set(),
    'цена': set(),
    'количество': set(),
    'ед': set(),
}
for i in items:
    res['название'].add(i[1]['название'])
    res['цена'].add(i[1]['цена'])
    res['количество'].add(i[1]['количество'])
    res['ед'].add(i[1]['ед'])
print(res)
