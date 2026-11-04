from lessons.l3.l3_task4 import title
from lessons.l8.blog import author


class Post:
    def __init__(self, title: str, text: str, author: str ) -> None:
        self.title = title
        self.text = text
        self.author  = author
        self.likes = 0
def display(self) -> None:
    print(f"Название {self.title} автор {self.author}")

@staticmethod

def is_valid(title: str) -> bool:
    return isinstance(title, str) and bool(title.strip())

@classmethod
def from_cvs(cls, row: str) -> "Post":
    title, author, text = row.strip(";")
    if not  cls.is_valid(title):
        raise ValueError("Не допустим")
    return cls(title, author, text)
post = Post.from_cvs("Занимательная физика; Алла; Млй первый пост. Мой второй пост")
post.display()

print(Post.is_valid("Занимательная математика"))
print(Post.is_valid(1))
print(post.is_valid_title(post.title))

title = input("Введите заголовок статьи ")
author = "Артем"
text = "Мой третий пост"

if Post.is_valid(title):




