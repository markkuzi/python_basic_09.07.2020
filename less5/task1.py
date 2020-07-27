import os

file = open('task1.txt', 'a', encoding='UTF-8')
while True:
    tps = input()
    if tps:
        file.write(tps + '\n')
    else:
        file.close()
        break
