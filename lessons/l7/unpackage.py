point = (10,20)
x, y = point
print(x)
print(y)
#* символ распаковвки поэлементно
first, *rest = (10, 20, 30, 40)
print(first)
a, b = 1,2
a, b = b, a
print(a, b)

pairs = [("name", "Екатерина"),("age", 30)]
for key, value in pairs:
    print(key, value)