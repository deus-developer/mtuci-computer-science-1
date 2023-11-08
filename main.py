from math import sqrt


def get_triangle_area(a: float, b: float, c: float) -> float:
    # Получение площади треугольника по трем сторонам, через формулу Герона
    # https://en.wikipedia.org/wiki/Heron%27s_formula

    p = (a + b + c) / 2
    area = sqrt(p * (p - a) * (p - b) * (p - c))

    return area


def is_triangle(a: float, b: float, c: float) -> bool:
    # Для любого треугольника выполняется неравенство треугольника:
    # сумма длин двух любых сторон треугольника всегда больше длины третьей стороны:
    # Если это неравенство не выполняется – треугольник не существует
    # https://en.wikipedia.org/wiki/Triangle_inequality
    
    return (
        a + b > c and
        a + c > b and
        b + c > a
    )


def main():
    # Длины сторон для построения треугольников
    sides = [3, 2, 4, 7, 5, 12, 11, 13, 15, 16, 14, 14]
    sides.sort(reverse=True)

    generator = (
        (sides[i], sides[j], sides[k])
        for i in range(len(sides))
        for j in range(i + 1, len(sides))
        for k in range(j + 1, len(sides))
    )

    area_generator = (
        get_triangle_area(a, b, c)
        for a, b, c in generator
        if is_triangle(a, b, c)
    )
    answer = max(area_generator)

    print("Максимальная площадь треугольника:", answer)


if __name__ == '__main__':
    main()
