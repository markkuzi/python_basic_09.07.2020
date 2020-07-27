import os

file = open('task2.txt', 'r')
count_line = 0
for line in file:
    count_line += 1
    count_word = 1
    for i in line:
        if i == ' ':
            count_word += 1
    print(f'В строке {count_line} находиться слов: {count_word}')
print(f'Всего строк: {count_line}')
file.close()
