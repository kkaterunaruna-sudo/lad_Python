list1 = [23, 89, 90, 45, 34, 23, 78, 56]
for grade in list1:
    if grade >= 90:
        print(f"Оценка {grade} Отлично")
    elif grade >= 70:
        print(f"Оценка {grade} Хорошо")
    elif grade >= 50:
        print(f"Оценка {grade} Удовлетворительно")
    else:
        print(f"Оценка {grade} Неудовлетворительно")

