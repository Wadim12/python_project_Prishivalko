# Функция invert_digits(k) меняет порядок цифр числа на обратный


def invert_digits(k):
    result = 0
    while k > 0:
        result = result * 10 + k % 10
        k //= 10
    return result


for _ in range(5):
    n = int(input('Введите целое положительное число: '))
    print(n, '->', invert_digits(n))