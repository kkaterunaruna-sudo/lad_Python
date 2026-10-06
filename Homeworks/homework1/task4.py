number = input("Введите число:")
try:
    number2 = int(number)
    print("Вы ввели число ")
except ValueError:
    print("Вы ввели не число.")

    