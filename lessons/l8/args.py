#неопределенный набор чисел"
#def sum_all(*numbers: tuple[int]) -> int:
def sum_all(*numbers: int) -> int:
    """
    складывает произвольное количество чисел
    :param numbers:
    :return:
    """
    #return sum(numbers)
    total = 0
    for num in numbers:
        total += num
    #print(total)
    return total

print(sum_all(4, 9, 8))

def print_config(**kwargs: dict[str, str] )->None:
    for key, value in kwargs.items():
        print(key, value)
print_config(key = "name", value = "Ivan", age = "20")

numbers = [1, 2, 3, 4, 5]
squared  = list(map(lambda x: x**2,numbers))
print(squared)

evens = list(filter(lambda x: x % 2 == 0,numbers))
print(evens)

articles = [
    {"title": "Python", "rating": 4.5},
    {"title": "Java", "rating": 3.5},
    {"title": "C++", "rating": 5.0},
]

#lambda это тоже самое что  def название функции(x)
#  то что возвращает эта функция  x["rating"]
by_rating = sorted(articles, key=lambda x: x["rating"])
print(by_rating)