import time
from functools import wraps

def time_it(func):
    """Декорратор измеряет время выполнения функции"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args,**kwargs)
        end = time.perf_counter()
        elapsed = end- start
        print(f"Функция {func.__name__} {func.__doc__} отработала за {elapsed:.6f} c.")
        return result
    return wrapper
def logged(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} , args = {args}, kwargs = {kwargs}")
        res = func(*args, **kwargs)
        print(f"Результат {func.__name__}: {res}")
        return res
    return wrapper
@logged
@time_it
def sum_of_list(numbers):
    """Считает сумму чисел"""
    return sum(numbers)

print(sum_of_list(range(100)))
