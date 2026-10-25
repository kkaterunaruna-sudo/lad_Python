from collections import Counter, defaultdict

posts =[
    (" Django", "IT", 2027),
    ("PostgreSQL", "DB", 2024),
    ("Viev ", "Django", 2026),
    ("Транзакции", "DB", 2025)
]


by_category= defaultdict(list)
for title, category, age in posts:
    by_category[category].append(title)
print(by_category["DB"])
print(by_category["New"])
categories = [post[1] for post in posts]
counts = Counter(categories)
print(counts)