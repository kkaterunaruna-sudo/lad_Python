from lessons.l3.l3_task1 import total

scores = {
    "Python": 90,
    "Django": 83,
    "Postgres": 60,
}
for course in scores:
    print(course)
for score in scores.values():
    print(f"{score}: {score}")
for score in scores.values():
    total += score
print(f"Cумма всех баллов  {total}")

print(scores.get("Flask", "Курса нет "))
print(scores.get("Django", "Курса нет "))



