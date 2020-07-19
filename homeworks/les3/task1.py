def my_divide(a, b):
    if b != 0:
        return print(a / b)
    else:
        return print('На 0 не делим')


while True:
    dividend = input('Введите делимое: ')
    try:
        dividend = float(dividend)
        break
    except ValueError:
        print('Делимое должно быть числом!')
while True:
    divisor = input('Введите делитель: ')
    try:
        divisor = float(divisor)
        break
    except ValueError:
        print('Делитель должно быть числом!')

my_divide(dividend, divisor)
