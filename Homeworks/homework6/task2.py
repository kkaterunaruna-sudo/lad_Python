#Агрегация «баллы за курс».
# Дан словарь scores с баллами по курсам (не менее 4 курсов).
# Напишите цикл по items(), который:
# выведет каждую пару в формате курс: балл;
#посчитает сумму баллов;
#через get() выведет значение для курса,
# которого в словаре нет, с запасным текстом.


scopes = {
    "Верстка сайтов (HTML и СSS)": 99,
    "JavaScript": 85,
    "GitHub": 60,
    "Сеть API": 78,
    "React": 67,
}
for course, score in scopes.items():
    print(f"{course}:{score}")
total = 0
for score in scopes.values():
    total +=score
print(f"Сумма баллов: {total}")
# total2 = sum(scopes.values())
# print(total2)
#Значение для курса
print(scopes.get("Angular", "Такого курса нет"))
course2 = input ("Введите название курса: ")
print(scopes.get(course2, "Такого курса нет"))