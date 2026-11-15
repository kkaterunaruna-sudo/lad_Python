import time
import functools

def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter() # считает точно
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} отработало за {elapsed:.6f} cек.") # дандр аргумент
        return result

    return wrapper

def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"вызов : {func.__name__}({args}), {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат {func.__name__}- {result}")
        return result
    return  wrapper

@logged
@time_it
def sun_of_list(numbers: list) :
    return sum(numbers)
print(sun_of_list.__name__)

@time_it
def min_of_list(numbers: list) :
    return min(numbers)
my_numbers = list(range(1000))
print(sun_of_list(my_numbers))
print(min_of_list(my_numbers))