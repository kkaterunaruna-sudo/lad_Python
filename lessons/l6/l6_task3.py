from collections import Counter

odd_sguares = {number:number **2 for number in range(10)if number % 2 !=0 }
words = ["Python", "Web"]
len_of_words = {word: len(word) for word in words}
print(len_of_words)

counter = Counter(words)
print(counter)
char_counter = Counter("Занимательная математика")
print(char_counter)