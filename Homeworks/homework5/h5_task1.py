test_scores = [9, 7, 4, 1 ,5, 2, 1, 5]
print(f"По убыванию: {test_scores}")
test_scores.sort(reverse=True)
print(f"Сумма всех баллов за тест {sum(test_scores)}")
print(f"Средний балл за тест {sum(test_scores)/ len(test_scores)}")
print(f"Минимальный  балл за тест {min(test_scores)}")
print(f"Максимальный балл за тест {max(test_scores)}")
