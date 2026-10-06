from lessons.l5.lists import categories

numbers = list(range(1, 11))
sguares = [num**2 for num in numbers]
print(f"Квадраты {sguares}  ")

evens = [num for num in numbers if num %2  == 0 ]
print(evens)
prices =[5689, 8976, 9876, 9087]
flags = [num > 5000 for num in prices]
print(prices, flags, sep ="\n")
categories = ["python", "django", "sql"]
