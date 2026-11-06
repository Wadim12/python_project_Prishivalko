#Вывести в порядке убывания все целые числа между А и В и их количество N

def read_int(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Неправильно ввели!")


def main():
    # Ввод чисел A и B; по условию должно выполняться A < B
    a = read_int("Введите A: ")
    b = read_int("Введите B: ")
    while a >= b:
        print("Должно выполняться A < B!")
        a = read_int("Введите A: ")
        b = read_int("Введите B: ")

    count = 0
    number = b - 1

    # Идём от B - 1 вниз до A + 1 (сами A и B не выводим)
    while number > a:
        print(number)
        count += 1
        number -= 1

    print("Количество чисел N =", count)


if __name__ == "__main__":
    main()


