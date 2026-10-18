#Множества: уникальные значения.
# Дан список тегов tags (с дублями).
# Составьте множество уникальных тегов через set, затем:

#проверьте, есть ли в нём конкретный тег через in;
#добавьте новый тег через add;
#удалите несуществующий тег через discard (без ошибки) и
# через remove в try/except — запишите, чем они отличаются,
# в комментарии.

tags = [1, 2, 8, 2, 3, 4, 3, 6, 5, 8, 6, 5, 2, 1, 9, 7, 8, 7, 6]
unique_tags = set(tags)
print(unique_tags)
print(7 in unique_tags)
unique_tags.add(22)
print(unique_tags)
unique_tags.discard(99)
unique_tags.discard(22)
print(unique_tags)


try:
    unique_tags.remove(99)
    print("Удалено ! ")
except KeyError:
    print("Вы ввели не существующий тег.")
#комментарии
# При удалении  несуществующий тег через discard (Программа не
# выводит ошибку )
# через remove в try/except — если элемент вызывает ошибку