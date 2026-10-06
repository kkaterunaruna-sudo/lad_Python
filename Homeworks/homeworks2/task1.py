num = int(input ("Введите целое число: "))
if num % 2 == 0 and num > 1:
    print("Число четное, положительное ")
    if num % 2 == 0 and num < 1:
        print("Число четное, отрицательное ")
elif num % 2 == 1 and num > 1:
    print("Число нечетное, положительное ")
elif num % 2 == 1 and num < 0:
    print("Число нечетное, отрицательное ")
else:
    print("Число равно нулю ")