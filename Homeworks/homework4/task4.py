post1 ="Работа с HTTP-заголовками в Python"
post2 = "Программирование на Python"
post3 = "Занимательная теория и практика "

post1 = " ".join(post1.split())
if  "Python" in post1:
    print(post1)
if  "Python" in post2:
    print(post2)
if  "Python" in post3:
    print(post3)

def build_slug(title:str) ->str:
#прошлись по символам все символы стали не заглвными а строчными
    result = title.lower()
    result = result.replace(" ", "-")
    clean = []
    for char in result:
        if char.isalnum() or char == "-":
            clean.append(char)
        else:
            clean.append("-")
    result ="".join(clean)
#собираем в том виде в котором есть из списка строку
#избавляемся от лишних --
    while "--" in result:
        result = result.replace ("--", "-")
#по обем сторонам удаляем
    result = result.strip("-")
    return result
print(build_slug(post1))
print(build_slug(post2))
print(build_slug(post3))