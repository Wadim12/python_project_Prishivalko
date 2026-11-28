# Проверка чередования положительных
# и отрицательных чисел

n = int(input('Введите размер списка: '))

a = []
i = 0

while i < n:
    a.append(int(input('Введите элемент списка: ')))
    i += 1

print('Исходный список:', a)

i = 1
result = 0

while i < n:
    if a[i] * a[i - 1] > 0:
        result = i + 1
        break
    i += 1

print('Результат:', result)