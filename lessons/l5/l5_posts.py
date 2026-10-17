from random import choice

# Меню блога (список постов).
# Заведите список постов
# — каждый пост это список [дата, заголовок, категория]
# (дата в формате ГГГГ-ММ-ДД).
# Выведите все посты, отсортируйте их по дате,
# а затем отфильтруйте по введённой с клавиатуры категории.
# Если в этой категории постов нет — выведите сообщение об этом.

posts = [
    ["2026-09-19", "Data Definition Language", "SQL"],
    ["2026-10-11", "Data Manipulation Language", "SQL"],
    ["2026-11-23", "Базовые коллекции ", "Python"],
    ["2026-12-19", "Архитектура MVT", "Django"],
    ["2027-01-10", "Архитектура и Базовые концепции", "Docker"],
]

print("Добро пожаловать!!!")
while True:
    print("Что делаем ?")
    print("1 - добавить пост")
    print("2 - показать все посты")
    print("3- отсортировать по дате")
    print("4 - отфильтровать по категории")
    print("5 - выйти")
    choice = input("Ваш выбор: ")
    if choice == "1":
        date = input("Дата (ГГГГ-ММ-ДД)")
        title = input("Заголовок: ")
        category = input("Категория")
        posts.append([date, title, category])
        print("Пост добавлен!")
    elif choice == "2":
        print("\nВсе посты: ")
        for post in posts:
            print(f"{post[0]} | {post[1]}  | {post[2]}")
    elif choice == "3":
        posts.sort()
        print("\nОтсортировано по дате: ")
        for post in posts:
            print(f"{post[0]} | {post[1]}  | {post[2]}  ")

    elif choice == "4":
        target = input("Какая категория?: ")
        filtered = [post for post in posts if post[2] == target]
        print(f"\n  Посты в категории {target}: ")
        if filtered:
            for post in filtered:
                print(f"{post[0]} | {post[1]}  | {post[2]}  | {post[3]} | {post[4]}")
        else:
            print("Постов в этой категории нет")
    elif choice == "5":
        print("Досвидания!")
        break
    else:
        print("Не понял команду введи уще раз.")    