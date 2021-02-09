print('Чтобы закончить ввод - оставьте строку пустой.')
with open('t1_text.txt', 'w') as fi:
    while True:
        ent = input('Введите данные:')
        fi.write(ent + '\n')
        if not ent:
            break
my_f = open('t1_text.txt', 'r')
print(my_f.read())
my_f.close()
