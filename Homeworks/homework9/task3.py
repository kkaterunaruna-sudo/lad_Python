from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} , args = {args}, kwargs = {kwargs}")
        res = func(*args, **kwargs)
        print(f"Результат {func.__name__}: {res}")
        return res
    return wrapper
articles = []
@logged
def create_article(title):
    articles.append(title)
    return title
@logged
def get_article(index):
    return articles[index]
@logged
def del_article(index):
    articles.pop(index)
create_article("Первая статья")
create_article("Вторая статья")
get_article(0)
del_article(1)