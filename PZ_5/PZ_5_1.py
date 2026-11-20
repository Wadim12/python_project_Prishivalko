# Построить изображение: в 1-й строке 1 звездочка, во 2-й 2, ..., в m-й m


def draw_triangle(m):
    for i in range(1, m + 1):
        print('*' * i)


m = int(input('Введите m: '))
draw_triangle(m)