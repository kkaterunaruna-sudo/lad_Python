print(bool(0)) # False  Python оценивает истинность, а ноль это всегда False
#bool тип данных основывается на числах.
# это подтип числа -имеет 2 значения: 0 1
# bool(1) True, bool(0) False
print(bool("0")) # True наличие данных в строке
print(bool(0.0)) #False автоматически
print(bool(" ")) #True наличие данных. Строка содержит пробел
print(bool("")) #False строка пустая
print(bool([ ])) #False список пустой
print(bool([1])) #True  список не пустой
print(bool({})) #False  кортеж пустой
print(bool(False)) #False
print(bool(None)) #False None - отсутствие данных
print(bool(True)) #True




