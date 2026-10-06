number = int(input("Введите число: "))
list1 = [34, 89, 87, 45, 34, 23, 56, 78, 67, 56, 34]
for i in list1:
    if i == number:
        print("Нашли")
        break
    else:
        print("Не нашла ни одного совпадения")

