def my_int_try(number):
    try:
        number = int(number)
        return True
    except ValueError:
        return False


def my_map(func, iter_object):
    result = []
    for i in iter_object:
        result.append(func(i))
    return result


def my_string_list(string):
    tps = ''
    tpl = []
    for i in string:
        if i == ' ':
            tpl.append(tps)
            tps = ''
            continue
        tps += i
    tpl.append(tps)
    return tpl


def my_func():
    sum = 0
    while True:
        numbers = input('Введите список целых числе через пробел, если хотите знакочить, введите *: ')
        numbers = my_string_list(numbers)
        for i in numbers:
            if my_int_try(i):
                i = int(i)
                sum += i
            elif i == '*':
                return print(sum)
            else:
                print(f'{i} - не является числом')


my_func()
