prices  = [130, 450, 34, 78, 90, 789, 1000, 432, 67, 90]
threshold = int(input("Введите цену порога: "))
list1 = [n< threshold  for  n in prices ]
list2 = [n for n in prices if n < threshold]
print(f"Количество  цен ниже порога{sum(list1)}")
print(f" Средняя цена по доступным позициям{sum(list2)/ len(list2)}")

