from main import is_published

post_title = "Питон"
post_text = "Питоны зеленые"
is_published = True #опубликован пост или нет
is_draft = False# черновик это статьи или нет
print(f"Пост: {post_title} ")
# if is_published and not is_draft:
#     print(f"Текст:{post_text} ")
# elif is_draft:
#     print("Статья в черновике")
# else:
#     print("Пост скрыт")

guest_age = int(input("Введите ваш возраст: "))
is_adult_only = False #статья для взрослых
is_allow_viev = True
if is_adult_only:
    # print("Доступ разрешен" if guest_age >= 18 else "доступ запрещен :(")
    if guest_age >= 18:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")


else:
    print("Ограничений нет ")
if is_allow_viev:
    if is_published and not is_draft:
        print(f"Текст:{post_text} ")
    elif is_draft:
        print("Статья в черновике")
    else:
        print("Пост скрыт")



