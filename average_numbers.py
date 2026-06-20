list_digits = list(map(int, input("Введите список чисел: ").split()))
s = 0
for i in list_digits:
    s = s+i
    average = s/len(list_digits)
    count = sum(1 for i in list_digits if i > average)
    above_average = tuple(i for i in list_digits if i > average)
print("Сумма = ", s)
print("Среднее = ", average)
print("Чисел больше среднего: ", count, above_average)
