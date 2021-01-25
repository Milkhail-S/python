time = int(input('Введите целое количество секунд: '))
h = time // 3600
m = (time - h * 3600) // 60
sec = time - h * 3600 - m * 60
print(f'{h:02d} : {m:02d} : {sec:02d}')
