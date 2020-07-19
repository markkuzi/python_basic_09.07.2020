def my_abs(number):
    if type(number) == int:
        number = str(number)
        if number[0] == '-':
            number = int(number[1:])
            return number
    elif type(number) == float:
        number = str(number)
        if number[0] == '-':
            number = float(number[1:])
            return number


def my_func1(a, b):
    return print(a ** b)


def my_func2(a, b):
    tmp = 0
    while tmp != my_abs(b):
        a = a / a
        tmp += 1
    #    for i in range(0, my_abs(b)):
    #        a = a / a
    return print(a)


my_func1(5, -5)
my_func1(5, -5)
