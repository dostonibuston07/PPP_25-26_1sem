import random

N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))

tab = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(random.randint(1, 99))
    tab.append(row)

print("\nСгенерированная таблица:")
for row in tab:
    print(row)

print("\nМаксимумы по строкам:")
row_max = []
for row in tab:
    max_value = max(row)
    row_max.append(max_value)
    print(max_value)

print("\nМаксимумы по столбцам:")
col_max = []
for col in range(M):
    column_values = []
    for row in range(N):
        column_values.append(tab[row][col])
    max_value = max(column_values)
    col_max.append(max_value)
    print(max_value)

main_diag_sum = 0
for i in range(min(N, M)):
    main_diag_sum += tab[i][i]

secondary_diag_sum = 0
for i in range(min(N, M)):
    secondary_diag_sum += tab[i][M - 1 - i]

print("\nСумма главной диагонали:", main_diag_sum)
print("Сумма побочной диагонали:", secondary_diag_sum)

max_sum = None
max_row_index = None

for i in range(N):
    row_sum = sum(tab[i])
    if (max_sum is None or row_sum > max_sum):
        max_sum = row_sum
        max_row_index = i

print("\nСтрока с наибольшей суммой элементов:")
print("Номер строки:", max_row_index)
print("Сумма:", max_sum)
print("Сама строка:", tab[max_row_index])
