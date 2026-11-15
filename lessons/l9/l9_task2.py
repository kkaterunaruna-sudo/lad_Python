import time
from functools import wraps
def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter() # считает точно
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} отработало за {elapsed:.6f} cек.") # дандр аргумент
        return result
    return wrapper
def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} c аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)

        print(f"Функция {func.__name__} вернула {result}.") # дандр аргумент
        return result
    return wrapper
@logged
@time_it
def sum_of_list(numbers: list) :
    return sum(numbers)

my_numbers = list(range(1000))
print(sum_of_list(my_numbers))



