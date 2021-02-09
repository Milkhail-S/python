f_name = 't4.txt'
f_name_new = 't4_2.txt'

new = {}
perevod = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
}
with open(f_name_new, 'w', encoding='utf-8') as f2:
    with open(f_name, 'r') as fi:
        for line in fi:
            pr = line.index(' ')
            f2.write(perevod.get(line[:pr]) + line[pr:])
