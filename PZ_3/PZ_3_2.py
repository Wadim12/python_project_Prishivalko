def read_int(prompt):
    s = input(prompt)
    while True:
        try:
            return int(s)
        except ValueError:
            print("Неправильно ввели!")
            s = input(prompt)


a = read_int("Введите a: ")
b = read_int("Введите b: ")
c = read_int("Введите c: ")

result = a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a
print("Треугольник существует:", result)