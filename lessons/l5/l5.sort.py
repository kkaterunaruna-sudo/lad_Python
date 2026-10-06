prices = [5689, 8976, 9876, 9087]
prices.sort()
print(f"По возрастанию: {prices}")
prices.sort(reverse=True)
print(f"По убыванию: {prices}")
prices = [5689, 8976, 9876, 9087]
sorted_prices = sorted(prices)
print(f"Исходный список: {prices}")
print(f"Отсортированный список: {sorted_prices}")

print(f"Сумма всех элементов списка {sum(prices)}")
print(f"Сумма всех элементов списка {min(prices)}")
print(f"Сумма всех элементов списка {max(prices)}")

affordable = [number for number in prices if number <= 5000]
affordable2 = [number for number in sorted_prices if number <= 5000]
print(f"Доступные суммы {affordable}")
print(f"Доступные суммы {affordable2}")

prices_strings = [str(number)  for number in sorted_prices]
print(prices_strings)

affordable.reverse()
print(affordable)
