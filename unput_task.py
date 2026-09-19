name = input("Привет . Как тебя зовут?  ")
age = int(input("Сколько тебе лет? "))
next_year_age = age +1
# print(f"Привет {name}, в следующем году тебе будет {next_year_age}")
# print("Привет {0}, в следующем году тебе будет {1}".format(name, age))

print("Привет {name}, в следующем году тебе будет {next_year_age}".format(name=name, next_year_age=next_year_age))