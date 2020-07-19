def my_func(a, b, c):
    if a < b and a < c:
        return print(b + c)
    elif b < a and b < c:
        return print(a + c)
    else:
        return print(a + b)


my_func(3, 5, 4)
