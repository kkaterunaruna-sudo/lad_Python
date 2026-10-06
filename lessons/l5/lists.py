categories = []

categories.append("Python")
categories.append("Django")
categories.append("SQL")
categories.extend(["Git", "Docker" ])
categories.insert(0, "Оглавление ")
print(categories)
print(len(categories))

print("Django" in categories)

print(categories.count("Git"))
print(categories.index("Docker"))
first = categories.pop(0)
print(f"Мы удалили {first}")

categories.remove("Git")
print(categories)

