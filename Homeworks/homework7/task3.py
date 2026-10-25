from collections import namedtuple



Post = namedtuple("Post", ["title", "category","year"])
posts =[
    Post(" Django", "IT", 2027),
    Post("PostgreSQL", "DB", 2024),
    Post("Viev ", "Django", 2026),
    Post("Транзакции", "DB", 2025)
]
posts.append(Post("Валидация", "DB", 2027))
print("Все статьи")
for post in posts:
    print(f"{post.title},{post.category}, {post.year}")
sorted_posts = sorted(posts, key=lambda post: post.year, reverse=True)

print("Статьи по годам")
for post in sorted_posts:
    print(f"[{post.year}][{post.category}] : [{post.title}]")
print("Статьи по категории ")
category = "DB"
matching = [post for post in posts if post.category == category]
print(f"Статьи и категории {category}: ")
for post in matching:
    print(f"{post.title}, {post.year}")