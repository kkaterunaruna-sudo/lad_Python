file = open("Notes.txt", "w", encoding="utf-8")
file.write("Моя первая заметка\n")
file.write("Моя вторая заметка\n")
file.close()


with open("Notes.txt", "r", encoding="utf-8") as f:
    content= f.read()
print(content)

with open("Notes.txt", "a", encoding="utf-8") as f:
    f.write("Моя третья запись\n")

with open("Notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"Строка: {line.strip()}")





