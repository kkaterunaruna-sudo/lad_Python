age = int(input("Введите ваш возраст: "))
if  0 <= age <= 12:
    print("Ребенок")
elif 13 <= age <= 17:
    print("Подросток")
elif 18 <= age <=64:
    print("Взрослый")
elif age < 0 or age > 150:
    print("Неправильно ввели возраст. Попробуйте еще раз!")
else:
    print("Пенсионер 65 +")


