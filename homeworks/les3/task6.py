alpha = {
    'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K',
    'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V',
    'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'

}


def my_split(string):
    tps = ''
    tpl = []
    for i in string:
        if i != ' ':
            tps += i
        else:
            tpl.append(tps)
            tps = ''
    tpl.append(tps)
    return tpl


def my_list(word):
    tml = []
    for i in word:
        tml.append(i)
    return tml


def my_join_word(list):
    tms = ''
    for i in list:
        tms += i
    return tms


def my_join_string(list):
    tms = ''
    for i in list:
        tms = tms + i + ' '
    return tms[:-1]


def my_map(func, iter_object):
    result = []
    for i in iter_object:
        result.append(func(i))
    return result


def int_func(word):
    word = my_list(word)
    word[0] = alpha[word[0]]
    return my_join_word(word)


def int_big_func(string):
    string = my_split(string)
    string = my_map(int_func, string)
    string = my_join_string(string)
    return string


while True:
    change = input('Если вы хотите одно слово, напишите "1", если предложение, то "2": ')
    if change == '1':
        your_word = input('Введите ваше слово маленькими латинскими буквами: ')
        accept = True
        for i in your_word:
            if i in alpha:
                accept = True
            else:
                accept = False
                print('Ошибка! Нужно вводить только маленькие буквы')
                break
        if accept:
            print(int_func(your_word))
    elif change == '2':
        your_word = input('Введите ваше предложение маленькими латинскими буквами без знаков препинания: ')
        accept = True
        for i in your_word:
            if i in alpha or i == ' ':
                accept = True
            else:
                accept = False
                print('Ошибка! Нужно вводить только маленькие буквы')
                break
        if accept:
            print(int_big_func(your_word))
    else:
        break
