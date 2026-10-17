point = (10, 20)
x, y = point
print(f"значениe х  {x}, значение y {y}")

first, *rest = (10, 20, 30, 40)
# *rest = (10, 20, 30, 40)
print(first)
print(rest)

a, b = 1, 2
a, b = b, a
print(a, b)

pairs =  [("name", "Екатерина"),("age", 20)]
for key, value in pairs:
    print(f"Ключ {key}, значение {value}")

