genes = []
with open("C:/Users/User/Desktop/Программы для Github/gene.txt", "r") as f:
    for line in f:
        name, length = line.strip().split()
        genes.append((name, int(length)))
avg = sum(length for name, length in genes) / len(genes)
long_genes = [name for name, length in genes if length > avg]

print("Средняя длина: ", avg)
print("Гены длиннее среднего: ", long_genes)
