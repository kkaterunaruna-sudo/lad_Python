import csv

rows = [
    ["title", "author", "views"],
    ["Занимательная физика", "Перельман", 120],
    ["Занимательная астрономия", "Перельман", 50],
    ["Занимательная математика", "Перельман", 98]

]


with open("Articles.csv", "w", encoding="cp1251", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

with open("Articles.csv", "r", encoding="cp1251") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)




