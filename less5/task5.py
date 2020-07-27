import os

file = open('task5.txt', 'w', encoding='UTF-8')

tps = input()
file.write(tps)
file.close()
file = open('task5.txt', 'r', encoding='UTF-8')
content = file.read()
file.close()
content = content.split()
summa = 0
for i in content:
    try:
        i = int(i)
        summa += i
    except ValueError:
        print('Значение не являктся целым числом.')
print(summa)
