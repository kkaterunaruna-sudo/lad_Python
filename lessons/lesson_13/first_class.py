class Post:
    def __init__(self, title: str, text: str, author: str ) -> None:
        self.title = title
        self.text = text
        self.author  = author
        self.likes = 0



first = Post(title="Занимательный Python", text="Первый текст", author="Pocco")
second = Post(title="Занимательная математика", text="Второй текст", author="Петров")


print(first.title)
print(second.title)
print(second.likes)


print(first is second)
print(type(first))
print(type(second))