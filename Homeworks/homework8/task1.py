

articles = []
def create_article(title, author, category, rating, views):
    """ Создает словарь статьи и добавляет его в список. Возвращает новую статью"""
    article = {
        "title": title,
        "author": author,
        "category": category,
        "rating": rating,
        "views": views,
    }
    articles.append(article)
    return article
def show_articles(article_list):
    """Выводит все статьи из переданного списка"""
    if not article_list:
        print("Список статей пуст.")
        return
    for i , article in enumerate(article_list, start=1):
        print(f"{i}, {article["title"]} - {article["author"]} , {article["category"]}, рейтинг {article["rating"]}, число просмотров {article["views"]}")



def filter_by_category(article_list, category):
    """Возвращает новый список по заданной категории"""
    return [article for article in article_list if article["category"] == category]


def sort_articles(article_list, key = "rating", reverse= False):
    """Возвращает новый список, отсортированный по полю -Кеу """
    return sorted(article_list, key= lambda a:a[key], reverse=reverse)

def sort_views(article_list, key = "views", reverse= False):
    """Возвращает новый список, отсортированный по полю -views """
    return sorted(article_list, key= lambda a:a[key], reverse=reverse)

def show_help():
    """ Показывает список доступных команд"""
    print("Команды: add, show, filter, sort, help, quit")
print("Мини-проект")
show_help()

while True:
    command = input("Введите команду:  ").strip().lower()
    if command == "add":
        title = input("Введите заголовок: ")
        author = input("Введите автора:  ")
        category = input("Введите категорию: ")
        rating = input("Введите рейтинг: ")
        try:
            rat = float(rating)
        except ValueError:
            print("Oшибка, рейтинг должен быть числом ! ")
            rating = 0.0

        views = int(input("Введите число просмотров : "))

        create_article(title, author, category, rating, views)
        print("Статья добавлена.")

    elif command == "show":
        show_articles(articles)

    elif command == "filter":
        category = input("Введите категорию: ")
        filtered = filter_by_category(articles, category)
        print(f"Статей в категории {category} : {len(filtered)}")

    elif command == "sort":
        key = input("Поле для сортировки: (title/author/category/rating/views): ")
        sorted_list = sort_articles(articles, key=key)
        show_articles(sorted_list)
        sorted_list2 = sort_views(articles, key=key)
        show_articles(sorted_list2)
        


    elif command=="quit":
        print("Выход")
        break
    else:
        print("Неизвестная команда Введите /help/")





