posts = [
    "публикация",
    "пульсирующая вселенная",
    "занимательная астрономия",
]
print("Свежие статьи")

for number, title in enumerate(posts, start=1):
    print(f"{number}. {title}")

print("\nКарточка  статьи")
for title in posts:
    print(f"{title} - {len(title)} символов ")

print("\nПоиск")
if "пульсирующая вселенная" in posts:
    print("Пост про 'пульсирующая вселенная ' есть в списке")
else:
    print("Такой статьи нет")
