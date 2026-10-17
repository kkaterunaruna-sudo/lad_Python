point =(10, 20)
color = "red", "green", "blue"
single = (5,)
print(type(single))
not_tuple = (5)
print(not_tuple)
print(len(color))
print(color[0])
print(color[1:])
print("red" in color)
print(color.index("green"))
if "green" in color:
    print(color.index("green"))
print(color.count("red")) #количество красных

try:
    color[0] = "yellow"
except TypeError as err:
    print(f"Нельзя изменить кортеж: {err}")


