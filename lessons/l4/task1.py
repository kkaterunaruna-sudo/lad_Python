title = "В мире животных"

print(title[5])
print(title[-2])
print(title[7:]) # ж с нуля
print(title[-8:]) # животных
print(title[2:6]) # мире
print(title[::-1]) # в обратном порядке развернули строку
print(title.lower())
print(title.upper())

dirty = "   жирафы ! . "
clean = dirty.strip("!.")# убираем по краям !если не будет пробела то ничего не убере
print(clean)

print(f" длина до {len(dirty)}, длина после {len(clean)}")
print(title.replace("животных", "роботов"))
print(title.replace("и", "ы")) #меняет все
# empty =  ""
# print(empty[0])

print(title.startswith("В"), title.endswith("животных")) # мы обращаемся к новой
# если хотим к клпии то обращаемся к измененным и присваиваем им переменную
print(title.find("животных")) #по первой букве выводит индекс
print(title.count("и"))

