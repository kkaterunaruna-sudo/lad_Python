from collections import Counter


#Dict comprehension + Counter. Для списка слов words:
#постройте словарь {слово: длина} через dict comprehension;
#посчитайте частоту встречаемости слов через Counter;
#выведите топ-3 самых частых слова через most_common(3).

words = ["React", "react", "Vue", "Angular", "Python", "Python", "django", "web", "django", "python"]
length_of_word = {w: len(words) for w in words}
print(length_of_word)
counter = Counter(words)
print(counter)
counter2 = Counter(w.lower() for w in words)
print(counter2)
print(counter.most_common(3))
print(counter2.most_common(3))




