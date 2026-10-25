def add(a: int, b: int) -> int:
    """
    Возвращает сумму двух чисел
    :param a:
    :param b:
    :return:
    """
    return  a + b
#ничего не возвращает т.к без return
def print_sum(a: int, b:int) ->None:
    """
    Выводит сумму сложения но не возвращает
    :param a:
    :param b:
    :return:
    """
    print(f"Cумма: {a+b}") #Cумма: 11
result_print = print_sum(2, 9)
print(result_print) #None



total = add(1,2)
print(total)
#внутри функции нет переменной смотрит в глобальную
message = "глобальная"
def show_message() -> None:
    print(message)
def make_local()->None:
    message = "Локальная"
    print(message)
show_message()
make_local()
print(message)
#изменяем глобальную переменнукю
counter = 0
def increment_counter() -> None:

#обращайся к этой переменной из глобальной области видимости
    global counter
    counter +=1
    print(counter)
increment_counter() #1
increment_counter() #2
increment_counter() #3
print(counter) #3


