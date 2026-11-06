#Проверить истинность высказывания: Точка с координатами (х, у) лежит в четвертой координатной четверти


#Функция ввода вещественного числа с проверкой корректности ввода
def read_float(prompt):
    s = input(prompt)
    while True:
        try:
            return float(s)
        except ValueError:
            print("Неправильно ввели!")
            s = input(prompt)

#Ввод координат точки
x = read_float("Введите x: ")
y = read_float("Введите y: ")

result = x > 0 and y < 0

#Вывод результата
print("Точка лежит в четвёртой четверти:", result)
