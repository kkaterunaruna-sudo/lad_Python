from collections import namedtuple



Post = namedtuple("Post", ["title", "category","year"])
posts =[
    Post("Модели Django", "IT", 2025),
    Post("Индексы в PostgreSQL", "DB", 2024),
    Post("Viev-функции ", "Django", 2026),
    Post("Транзакции", "DB", 2025)
]
posts.append(Post("Формы и валидации", "Django", 2026))
print("Все статьи")
print(posts)
for post in posts:
    print(f"[{post.year}][{post.category}] : [{post.title}]")
    
   
#год как ключ для сотировки    
sorted_posts = sorted(posts, key=lambda post: post.year)

print("Статьи по годам")
for post in sorted_posts:
    print(f"[{post.year}][{post.category}] : [{post.title}]")
print("Статьи по категории ")
category = "DB"
matching = [post for post in posts if post.category == category]
