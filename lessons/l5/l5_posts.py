from random import choice

posts = [
    ["2026-02-10", "Как установить uv", "Инструментарий"],
    ["2026-02-14", "Списки в Python", "Python"],
    ["2026-02-18", "Введение в Django", "Django"],
]

print("Добро пожаловать в блог CLI")
while True:
    print(
        """
        Что делаем?
        1 - Доб пост
        2- Показать все посты
        3- Отсортировать по дате
        4 - Отфильтровать категории
        0 - Выйти
        

        """
    )
    choice = input("Ваш выбор: ")
    if choice ==1:
        new_date = input("Введите дату в формате ГГГГ-ММ -ДД: ")
        new_title = input("Введите заголовок ")
        new_title = input("Введите категорию ")
        posts.append([new_date], )

        
    
    