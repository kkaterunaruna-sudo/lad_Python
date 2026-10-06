text =" А роза упала на лапу Азора "
clean = text.strip(" ")
print(clean)
normalized = "".join(clean.split()).lower()
print(normalized)
if normalized==normalized[::-1]:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
