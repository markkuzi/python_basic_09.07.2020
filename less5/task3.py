import os

database = {

}
file = open('task3.txt', 'r', encoding='UTF-8')
content = file.readlines()
for i in content:
    tpl = i.split()
    tpl[1] = float(tpl[1])
    database[tpl[0]] = tpl[1]
sum_wage = 0
min_wage = 20000
workers = 0
for key, val in database.items():
    sum_wage = + val
    workers = + 1
    if val < min_wage:
        print(f'Сотрудник {key} получает оклад менее, чем {min_wage}.')
middle_wage = sum_wage / workers
print(f'Средний оклад сотрудников составляет: {middle_wage}.')
file.close()
