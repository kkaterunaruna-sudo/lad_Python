#Меню блога (список постов). 
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
    print("1 - показать все посты")
    print("2- отсортировать по дате")
    print("3 - отфильтровать по категории")
    print("4 - выйти")
    choice = input("Ваш выбор: ")

    if choice == "1":
        print("\nВсе посты: ")
        for post in posts:
            print(f"{post[0] } | {post[1]}  | {post[2] }")
    elif choice == "2":
        posts.sort()
        print("\nОтсортировано по дате: ")
        for post in posts:
            print(f"{post[0]} | {post[1]}  | {post[2]}  ")
            
    elif choice == "3":
        target = input("Какая категория?: ")
        filtered = [post for  post in posts if post[2] == target]
        print(f"\n  Посты в категории {target}: ")
        if filtered:
            for post in filtered:
                print(f"{post[0]} | {post[1]}  | {post[2]}")
        else:
            print("Постов в этой категории нет")
    elif choice == "4":
        print("Досвидания!")
        break
    else:
        print("Не понял команду введи уще раз.")