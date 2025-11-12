# Створення матриці 5x5 з послідовностями чисел від 1 до 5
matrix = []
for i in range(5):
    row = list(range(1, 6))  # Створюємо рядок [1, 2, 3, 4, 5]
    matrix.append(row)

print("Початкова матриця 5x5:")
for row in matrix:
    print(row)

# Заміна парних чисел на "P", непарних на "N"
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0:  # Перевірка на парність
            matrix[i][j] = "P"     # Парне число
        else:
            matrix[i][j] = "N"     # Непарне число

print("\nМатриця після заміни:")
for row in matrix:
    print(row)