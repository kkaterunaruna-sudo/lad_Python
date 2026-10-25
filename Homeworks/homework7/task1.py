person= ("Наташа","20","Москва")
print(type(person))
print(len(person))
print(person[0])
print(person[1:])

single = (5,)
# <class 'tuple'>
print(type(single))
single[0] = 6
#single[0] = 6

#TypeError: 'tuple' object does not support item assignment

#<class 'int'>
not_tuple = (5)
print(type(not_tuple))