#Словарь «профиль». Создайте словарь с данными пользователя
# (имя, возраст, город, профессия). Затем:
#выведите значение по ключу и через get() с запасным значением;
#проверьте через in, есть ли в словаре ключ "phone";
#добавьте ключ "email" и измените значение "age";
#удалите один ключ через pop и выведите получившийся словарь.
user = {
    "name":"Екатерина",
    "age":"25",
    "city":"Ульяновск",
    "job": "Учитель"
}

print(user.get("name", "нет"))
print(user.get("age", "нет"))
print(user.get("city", "нет"))
print(user.get("job", "нет"))
# print(user["name"])
print("phone" in user)
user["email"] = "test@mail.ru"
user["age"] = "26"
city2 = user.pop("city", "не задан")
print(f"city удален {city2}")
phone2 = user.pop("phone", "не задан")
print(f"phone удален {phone2}")
print(user)


