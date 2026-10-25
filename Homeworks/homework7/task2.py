numbers = (10, 20, 30, 40, 50)
a, *b, c = numbers
print(a)
print(b)
print(c)

name = "Иван"
first, *rest = name
print(first) # И
print(rest) #['в', 'а', 'н']