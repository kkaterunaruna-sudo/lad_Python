#анотация только для разработчиков но это элемент валидации
#аргумент соглашение для разработчиков
def great(name: str)-> None:
    """
    Выводит приветствие по имени
    :param name:
    :return:
    """
    print(f"Hello, {name}")
# след функция должна писаться до всех вызовов


def user_info(name: str, age: int) -> None:
    """Выводит имя и возраст пользователя"""
    print(f"Hello, {name} {age}")

def great_full(name: str, greeting: str = "Привет")->None:
    print(f"{greeting} {name} !")

#Второй аргумент по умолчанию
great_full("Катя")
#все имеенованные в конце(ключевые) явно определяем значения
great_full("Иван", greeting="hello")



#когда не пишем кавычки пытаемся передать переменную а переменной Bob нет
great("Маша")
great(name="bob")
user_info("Мария", 45)
user_info(age=89, name="Мария")



