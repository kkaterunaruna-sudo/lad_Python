#Проверка доступа к посту
post_title = "Теория и практика."
post_text = "Tеория и практика археологических исследований."
is_published = True # Опубликован ли пост
is_premium = False #  пост премиальный
has_subscription  = False #  у пользователя есть подписка
print(f"Пост: {post_title} ")
print("Есть ли статья для отображения: ", bool(post_text))
can_show =  post_text and is_published and ( not is_premium or has_subscription)
if can_show:
    print(f"Показывает текст: {post_text}")
else:
    print("Пост скрыт")

