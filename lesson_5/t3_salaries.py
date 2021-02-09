f_name = 't3_salaries.txt'

fi = open(f_name, 'r', encoding='utf-8')
salary = []
for line in fi:
    salary.append(line.split())
print(salary)
print(f'Сотрудники с окладом менее 20000:')
sum = 0
for i in range(len(salary)):
    sum += int(salary[i][1])
    if int(salary[i][1]) < 20000:
        print(f'{salary[i][0]}')
print(f'Средняя зарплата сотрудников: {sum / len(salary):.2f}')
fi.close()
