import functools
import time


# --- «Данные» блога в памяти (персистентность — позже, на занятии 11) ---
articles = [
    {"id": 1, "title": "Первая запись", "author": "Иван"},
    {"id": 2, "title": "Как настроить uv", "author": "Мария"},
    {"id": 3, "title": "Зачем нужны декораторы", "author": "Иван"},
]


def logged(func):
    """Декоратор логирования действий со статьями — добавляет вывод «вокруг»."""

    @functools.wraps(func)                 # сохраняем метаданные исходной функции
    def wrapper(*args, **kwargs):
        print(f"> Действие: {func.__name__} ...")
        result = func(*args, **kwargs)
        print(f"> Готово: {func.__name__} -> {result}")
        return result

    return wrapper


def time_it(func):
    """Декоратор: измеряет время выполнения функции func."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"(время {func.__name__}: {end - start:.6f} с.)")
        return result

    return wrapper


@logged                        # добавляем логирование
@time_it                       # и замер времени — применяются снизу вверх
def list_articles():
    """Печатает все статьи блога."""
    for article in articles:
        print(f"[{article['id']}] {article['title']} — {article['author']}")
    return f"Всего статей: {len(articles)}"


@logged
def add_article(title, author):
    """Добавляет статью в список."""
    new_id = max(article["id"] for article in articles) + 1
    article = {"id": new_id, "title": title, "author": author}
    articles.append(article)
    return f"Добавлена статья #{new_id}"


@logged
def find_article(article_id):
    """Возвращает заголовок статьи по id или None."""
    for article in articles:
        if article["id"] == article_id:
            return article["title"]
    return None


# --- Демонстрация: логирование и замер делает декоратор, а не тело функций ---
list_articles()
add_article("Четвёртая запись", "Пётр")
find_articl(2)