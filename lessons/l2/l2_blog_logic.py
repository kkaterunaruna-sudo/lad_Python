post_text = "Привет" #есть ли текст
is_published = True # Опубликована ли статья
is_premium = False #  прекмимум есть
has_subscription = False # есть подписка или нет

print("Есть ли статья для отображения: ", bool(post_text))

can_show =  post_text and is_published and (is_premium or has_subscription)
if can_show:
    print(f"Показвавет текст: {post_text}")
else:
    print("Пост скрыт")
# может отображаться? проверка есть ли текст в статье ,опубликована ли она
# Eсть ли у пользователя премиум или подписка

autor_name = input("Имя автора(можно пусто): ")
display_name = autor_name or "Аноним"
print(f"Автор {display_name}")
age = int(input("Введите сколько вам лет? "))
if 0<=age <= 100:
    print("Возраст корректен")
else:
    print("Возраст некорректен")
