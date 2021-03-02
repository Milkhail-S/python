class Date:
    date = '31-11-20'
    day = 0
    month = 0
    year = 0

    @classmethod
    def date_extract(cls):
        cls.day, cls.month, cls.year = cls.date.split('-')
        return int(cls.day), int(cls.month), int(cls.year)

    @staticmethod
    def check():
        Date.date_extract()
        if int(Date.day) > 31 or int(Date.day) < 1:
            print(f'Вы ввели {Date.day}, число может быть в пределах от 1 до 31, соответстенно месяцу')
        if int(Date.month) > 12 or int(Date.month) < 1:
            print(f'Вы ввели {Date.month}, месяц может быть в пределах от 1 до 12')
        if int(Date.year) > 21:
            print(f'Вы ввели {Date.year}, год не может быть в будущем')

Date.date_extract()
Date.check()
print(f'День: {Date.day}\nМесяц: {Date.month}\nГод: 20{Date.year}')
