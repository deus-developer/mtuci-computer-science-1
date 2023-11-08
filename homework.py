from math import sqrt
from typing import List


def solve(a: float, b: float, c: float) -> List[float]:
    # Решение квадратного уравнения
    # https://en.wikipedia.org/wiki/Quadratic_equation

    discriminant = b ** 2 - 4 * a * c
    solutions: List[float] = []

    if discriminant < 0:
        return solutions

    discriminant_sqrt = sqrt(discriminant)
    double_a = 2 * a

    solutions.append(
        (-b - discriminant_sqrt) / double_a
    )

    if discriminant > 0:
        solutions.append(
            (-b + discriminant_sqrt) / double_a
        )

    return solutions


def main():
    print("Введите 3 коэффициента квадратного уравнения, например: 1.0 2.0 3.0")
    input_value = input("Коэффициенты: ")

    a, b, c = map(float, input_value.split())

    solutions = solve(a, b, c)

    if not solutions:
        print("Нет решений")
        return

    for idx, solution in enumerate(solutions, 1):
        print(f"X{idx} = {solution}")


if __name__ == '__main__':
    main()
