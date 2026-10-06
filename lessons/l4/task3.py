#валидация
#очищаем вероятные пробелы


raw_age = input("Сколько тебе лет? ").strip()
#проверяем на то что только цифры если будут символы не зайдет в иф
if raw_age.isdigit():
    age = int(raw_age)
    print(f"Ваш возраст {age}")
else:
    print("Возраст должен быть числом!")
login = input("Введите ваш логин ").strip()
# проверяем наличие букв и цифр но примет и то и то
if login and login.isalnum():
    print(f"Логин принят  {login}")
else:
    print("Логин должнен содержать буквы и цифры")

full_name = input("Ваше полное имя ФИО ").strip()
# он по умолчанию делит на пробелы можно не указывать делаем из строки список
parts = full_name.split(" ")
#проверяем количество элементов в списке
##########
if len(parts) == 3:
    surname,name,midlename = parts
    print(f"Фамилия: {surname}, Имя: {name}, Отчество: {midlename}")
else:
    print("Введите полное имя ")



