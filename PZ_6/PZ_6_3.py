# Поиск точки с минимальной суммой расстояний
# до остальных точек

import math

n = int(input('Введите количество точек: '))

x = []
y = []
i = 0

while i < n:
    print('Введите координаты точки', i + 1)

    x.append(float(input('X = ')))
    y.append(float(input('Y = ')))

    i += 1

min_sum = float('inf')
best_index = 0

i = 0

while i < n:
    total = 0
    j = 0

    while j < n:
        if i != j:
            distance = math.sqrt(
                (x[j] - x[i]) ** 2 +
                (y[j] - y[i]) ** 2
            )
            total += distance

        j += 1

    if total < min_sum:
        min_sum = total
        best_index = i

    i += 1

print('Искомая точка:')
print('X =', x[best_index])
print('Y =', y[best_index])
print('Минимальная сумма расстояний:', round(min_sum, 2))