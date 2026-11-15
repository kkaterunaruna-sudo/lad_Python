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

@time_it
def sord_of_list(numbers):
    """Сортирует список с декоратором"""
    return sorted(numbers)

def sord_of_list1(numbers):
    """Сортирует список без декоратора"""

    return sorted(numbers)
num = [5, 7, 9, 3, 1, 0, -1]
print(sord_of_list(num))
print(sord_of_list1(num))
#Функция sord_of_list Сортирует список с декоратором отработала за 0.000002 c.
#[-1, 0, 1, 3, 5, 7, 9]
#[-1, 0, 1, 3, 5, 7, 9]
