def make_multiplier(multiplicator: int):
    def multiply(number: int) -> int:
        return  number * multiplicator
    return multiply
# функция возвращаеи другую функцию

double = make_multiplier(2) # нах функция мультиплай ссылается на multiply
#из переменной сделали функцию  где первая функция является ссылкой на 2
print(double(10))
print(double(50))

tripple = make_multiplier(3)
print(tripple(10))
print(tripple(50))

def make_counter(start: int=0 ):
    count = start
    def increment(step: int=1) -> int:
        nonlocal count
        count += step
        return count
    return increment

counter = make_counter()
print(counter())
print(counter(10))
print(counter(20))#31

counter2 = make_counter(5)
print(counter2(10)) #15
print(counter2(10)) #25
print(counter()) #32



