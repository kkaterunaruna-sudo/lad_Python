from blog import data


def create_post_menu() -> None:
    title = input("Введите название статьи: ")
    author = input("Введите автора: ")
    text = input("Введите текст статьи: ")
    data.create_post(title, author, text )
    print(f"Статья {title} сохранена")


def show_posts_menu() -> None:
    posts = data.list_posts()
    if not posts:
        print("Статей нет")
        return
    for post in posts:
        print(f"{post["author"]} - {post["title"]} - {post["text"]}")




