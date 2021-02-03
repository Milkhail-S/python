def user_profile(name='не указано', surname='не указано', birthyear='не указано', city='не указано', email='не указано', tel='не указано'):
        return f'Имя: {name}, Фамилия: {surname}, год рождения: {birthyear}, город проживания: {city}, эл. почта: {email}, телефон: {tel}'


prof = user_profile(name=input('Введите имя:'), surname=input('Введите фамилию:'), birthyear=input('Укажите год рождения:'), city=input('Укажите город проживания: '), email=input('Укажите email: '), tel=input('Контактный телефон: '))
print(prof)
