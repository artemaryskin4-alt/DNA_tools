DNA_seq = input("Введите последовательнлость ДНК: ").upper()
valid_bases = set("ATGC")
while True:
    invalid_chars = [ch for ch in DNA_seq if ch not in valid_bases]
    if not invalid_chars:
        break  # всё в порядке
    print(f"Ошибка: недопустимые символы: {', '.join(set(invalid_chars))}")
    print("Разрешены только A, T, G, C.")
    DNA_seq = input("Введите последовательность ДНК заново: ").upper()
motif = input("Введите мотив для поиска: ").upper()
start = 0
position = []

while True:
    pos = DNA_seq.find(motif, start)
    if pos == -1:
        break
    start = pos + 1
if position:
    print("Мотив", motif, "Найден на позициях", positions)
else:
    print("Мотива", motif, "не найдено")
