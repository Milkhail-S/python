with open('t5.txt', 'w+') as fi:
    fi.write('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15')
    fi.seek(0)
    num = str(fi.read()).split()
    summary = [int(i) for i in num]
    print(f'Сумма чисел из файла равна = {sum(summary)}')
