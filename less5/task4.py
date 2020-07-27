import os

translate_base = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

file = open('task4.txt', 'r', encoding='UTF-8')
content = file.readlines()
translated_lines = []
for i in content:
    tps = i.split()
    tps[0] = translate_base[tps[0]]
    tps = ' '.join(tps)
    translated_lines.append(tps)
translated_lines = '\n'.join(translated_lines)
file.close()
new_file = open('new_task4.txt', 'w', encoding='UTF-8')
new_file.write(translated_lines)
new_file.close()
