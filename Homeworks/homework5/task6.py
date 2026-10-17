#Звёздочка (самостоятельное изучение key=lambda).
# Изучите по официальной документации Python,
# как работает sorted(..., key=...) и что такое lambda.
# Отсортируйте список постов из задачи 3:
# а) по длине заголовка; б) по категории (по алфавиту);
# в) по заголовку в обратном порядке.
# Объясните комментарием в коде,
# что возвращает key-функция в каждом случае.

posts = [
    ["2026-09-19", "Data Definition Language", "SQL"],
    ["2026-10-11", "Data Manipulation Language", "SQL"],
    ["2026-11-23", "Базовые коллекции ", "Python"],
    ["2026-12-19", "Архитектура MVT", "Django"],
    ["2027-01-10", "Архитектура и Базовые концепции", "Docker"],
]
sorted_posts = sorted(posts, key=lambda i: len(i[1]))
print(sorted_posts)
category_posts = sorted(posts, key=lambda i: i[2])
print(category_posts)

title = sorted(posts, key=lambda i: i[2], reverse = True)
print(title)