def info(name, surname, year, city, email, phone_number):
    return print(name, surname, year, city, email, phone_number)


person_template = {
    'имя': str,
    'фамилия': str,
    'год рождения': int,
    'город проживания': str,
    'email': str,
    'номер телефона': int
}
person_info = []

for key, val in person_template.items():
    while True:
        user_value = input(f'{key}: ')
        try:
            user_value = val(user_value)
        except ValueError as e:
            print(f'{e}\nНекорректный ввод!')
            continue
        person_info.append(user_value)
        break

name, surname, year, city, email, phone_number = person_info
info(name=name, surname=surname, year=year, city=city, email=email, phone_number=phone_number)
