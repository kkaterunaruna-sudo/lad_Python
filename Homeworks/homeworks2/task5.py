#программа проверки данных пользователя.
# (логин, пароль, возраст, email).
login = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")
age = input("Введите ваш возраст: ")
email = input("Введите ваш email")


if 3 <= len(login) <= 20:
    print("Логин валидный")
else:
    print("Логин не валидный ")
if  " " not in password:
    print("Пароль валидный ")
else:
    print("Пароль не валидный")
if "@" in email:
    print("Корректный email")
else:
    print("В адресе пропущена собачка ")
if age.isdigit():
    print("Успешно")
else:
    print("Введите число ")
passed = login and password and age and email
if passed:
    print("Пользователь зарегистрирован")
else:
    print("Пользователь не зарегистрирован")
