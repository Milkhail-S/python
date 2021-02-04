from sys import argv


script_name, hours, stavka, bonus = argv
salary = int(hours) * float(stavka) + int(bonus)
print(f'Заробатная плата сотрудника составила {salary:.2f} руб')
