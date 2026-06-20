#Ввод последовательности ДНК
DNA_seq = input("Введите последовательность ДНК: ").upper()
valid_bases = set("ATGC")

#Проверка ввода
while True:
    invalid_chars = [ch for ch in DNA_seq if ch not in valid_bases]
    if not invalid_chars:
        break  # всё в порядке
    print(f"Ошибка: недопустимые символы: {', '.join(set(invalid_chars))}")
    print("Разрешены только A, T, G, C.")
    DNA_seq = input("Введите последовательность ДНК заново: ").upper()

#Перевод ДНК в РНК
RNA_seq = DNA_seq.replace("T", "U")
print("Последовательность РНК: ", RNA_seq)
