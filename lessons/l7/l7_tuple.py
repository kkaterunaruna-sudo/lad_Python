point =(10, 20)
color = "red", "green", "blue"
single = (5,)
print(type(single))
not_tuple = (5)
print(type(not_tuple))
print(len(color))
print(color[0])
print(color[1:])
print("red" in color)
print(color.index("green"))
if "green" in color:
    print(color.index("green"))
print(color.count("red")) #количество красных
# пытаемся поменять элемент ПЫТАЕИМЯ
# ОЖИДАЕМ ЧТО ТАМ МБ ОШИБКА
# ЕСЛИ ВСЕ ХОРОШО ИДЕМ
# ДАЛЬШ
# ЕСЛИ ПЛОХО ОТБОТАТЫВАЕТ КОД ЕxCEPT(ОТЛОВ ИСКЛЮЧЕНИЕ) ГДЕ
# МВ ПРОПИСЫВАЕМ НАЗВАНИЯ исключения МОЖНО ПИСАТЬ ОБЩЕЕ
# ЭКСЕПШИОН это ощие иск(это плохо общую ошибку но когда не знаешь что моржет
# что можетупасть ,потом после тестирования
# заменять на точечные
# ошибки помещаем результат исключения в err
# присваиваем что то чему то
try:
    color[0] = "yellow"
except TypeError as err: #ОШИБКА КОТОРАЯ ВЫШЛА
    print(f"Нельзя изменить кортеж: {err}")
