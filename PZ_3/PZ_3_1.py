def read_float(prompt):
    s = input(prompt)
    while True:
        try:
            return float(s)
        except ValueError:
            print("Неправильно ввели!")
            s = input(prompt)


x = read_float("Введите x: ")
y = read_float("Введите y: ")

result = x > 0 and y < 0
print("Точка лежит в четвёртой четверти:", result)
