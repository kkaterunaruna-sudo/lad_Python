

articles = []

def create_articles(title: str, author: str,category: str,rating: float) -> dict:
    """
    Создается словарь статьи и добавляет его в список
    :param title:
    :param author:
    :param category:
    :param rating:
    :return:
    """
    article = {
        "title": title,
        "author": author,
        "category": category,
        "rating": rating

    }
    articles.append(article)
    return article
def show_articles(articles_list: dict) ->None:
    """
    Выводит все статьи
    :param articles:
    :return:
    """
    if not articles_list:
        print("Список статей пуст")
        return

    for num, article in enumerate(articles_list, start=1):
        print(f"{num}, {article["title"]}, Aвтор {article["author"]},"
              f"Категория {article["category"]}, Рейтинг {article["rating"]}")

    def filter_by_category(articles_list: list, category: str)-> list:
        """
        Возвращает статьи выбранной категории
        :param articles_list:
        :param category:
        :return:
        """
        return [article for article  in articles_list if article["category"] == category]
    def sort_articles(articles_list, key: str = "rating", reverse: bool = False)-> list:
        """Возвращает отсортированный список"""
        return sorted(articles_list, key=lambda x: x[key], reverse=reverse)

    def show_help() -> None:
        """Показывает список доступных команд"""
        print("""
        Доступные команды:
        add - Добавить статью
        show - Показать все статьи
        filter - Отфильтровать статьи по категории
        sort - Отсортировать статьи 
        help - Показать справку
        exit - Выйти
        """)
    print("Проект СlI")
    show_help()
while True:
    command = input("Введите команду: ").strip().lower()
    if command == "add":
        title = input("Заголовок: ")
        author = input("Автор: ")
        category = input("Категория: ")
        rating  = float(input("Рейтинг: "))
        create_articles(title, author, category, rating)
        print("Статья добавлена")
    elif command == "show":
        show_articles(articles)

    elif command ==  "filter":
        category = input("Категория")
        filtered_articles = filter_by_category(articles, category)
        print(f"В категории {category} {len(filtered_articles)} cтатей")
        show_articles(filtered_articles)

    elif command == "sort":
        key= input("Поле для сортировки (title, author, category, rating")
        reverse = input("Сортировать по убыванию")
        if reverse:
            reverse = True
        else:
            reverse = False
        sort_articles = sort_articles(articles, key, reverse)
        show_articles(sort_articles)

    elif command == "help":
        show_help()
    elif command == "exit":
        print("выход")
        break
    else:
        print("Команда неизвестная введити t")





