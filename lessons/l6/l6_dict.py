from pprint import pprint

user = {
    "name": "Екатерина",
    "age": 30,
    "city": "Ульяновск",
}

print(user["name"])
print(user.get("phone", "нет телефона"))
print("name" in user)
print("phone" in user)

# user["email"] = "test@mail.ru"
user["age"] = 29
pprint(user)

password = user.pop("email", "не задан")
print(password)

for key, value in user.items():
    print(f"{key}: {value}")
