import json

post={
    "title": "Моя первая статья",
    "author": "Анна",
    "tags":["Python", "JSON", "файлы"],
    "published": True,
    "views":120,


}
with open("post.json", "w", encoding="utf-8") as f:
    json.dump(post, f, ensure_ascii=False, indent=2)
with open("post.json", "w", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["title"])
