
number = int(input("Введите число: "))
factorial1 = 1
for i in range(1, number+1):
    factorial1*= i

    # print(factorial1)
    for y in range (1, 11):
        print(f"{i} * {y} = {i * y}")
print(f" факториал {factorial1}")

