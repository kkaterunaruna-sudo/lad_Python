post_title = "Питон"
post_text = "Питоны зеленые"
is_published = True #опубликован пост или нет. флаг
is_draft = False# черновик это статья или нет
print(f"Пост: {post_title} ")
# if is_published and not is_draft:
#     print(f"Текст:{post_text} ")
# elif is_draft:
#     print("Статья в черновике")
# else:
#     print("Пост скрыт")
#возраст гостя
guest_age = int(input("Введите ваш возраст: "))
is_adult_only = True # ограничения по возрасту (статья для взрослых)
is_allow_viev = False #  если нет ограничений выводим доступно к просмотру
if is_adult_only:
    # print("Доступ разрешен" if guest_age >= 18 else "доступ запрещен :(")
    if guest_age >= 18:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")
        is_allow_viev = False


else:
    print("Ограничений нет ")
#########
if is_allow_viev:
    if is_published and not is_draft:
        print(f"Текст:{post_text} ")
    elif is_draft:
        print("Статья в черновике")
    else:
        print("Пост скрыт")



