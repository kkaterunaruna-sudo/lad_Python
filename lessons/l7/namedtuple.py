from collections import namedtuple


Person = namedtuple("Person", ["name", "age", "city"])
# позиционные аргументы
ivan = Person("Ivan", 25, "Moscow")
# явно задали названия ключей можем распологать в любом порядке
anna = Person(name="Anna", age=20, city="Ульяновск")


print(ivan.name)
print(anna.age)
print(ivan)
#Person(name='Ivan', age=25, city='Moscow')
#поля выводим
print(Person._fields)
print(ivan._asdict())
ivan_next_year = ivan._replace(age=26)
print(ivan.age, ivan_next_year)
#25 Person(name='Ivan', age=26, city='Moscow')
#создал копию кортежа иван с замененным значением
print(ivan.age, ivan_next_year.age) #25, 26



