import os
import re

lessons_base = {

}
file = open('task6.txt', 'r', encoding='UTF-8')
content = file.readlines()
file.close()
for i in content:
    tps = i.split(':')
    nums = re.findall(r'\d+', i)
    nums = [int(i) for i in nums]
    lessons_base[tps[0]] = sum(nums)
print(lessons_base)
