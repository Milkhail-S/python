class Worker:
    def __init__(self, name, surname, position, salary=None, bonus=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'salary': salary,
            'bonus': bonus,
            }

class Position(Worker):
    def __init__(self, name, surname, position, salary, bonus):
        super().__init__(name, surname, position, salary, bonus)

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surname}\nРаботает {self.position}')

    def get_total_income(self):
        netto = self._income.get('salary') + self._income.get('bonus')
        print(f'Доход сотрудника составляет {netto}')

employee = Position('Илон', 'Маск', 'Инженер', 100.5, 200.5)
print(employee.name)
print(employee.surname)
print(employee.position)
print('Жалование: ', employee._income['salary'])
print('Премия: ', employee._income['bonus'])

employee.get_full_name()
employee.get_total_income()
