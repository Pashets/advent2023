from math import sqrt, ceil


def task_1(rows):
    result = 1
    for time, distance in zip(
            map(int, rows[0].split()[1:]),
            map(int, rows[1].split()[1:])
    ):
        x1 = (time + sqrt(time ** 2 - 4 * distance)) / 2
        x2 = time - x1
        x1, x2 = sorted([x1, x2])
        x1, x2 = ceil(x1), ceil(x2)
        result *= x2 - x1
    return result


def task_2(rows):
    time = int(''.join(rows[0].split()[1:]))
    distance = int(''.join(rows[1].split()[1:]))
    x1 = (time + sqrt(time ** 2 - 4 * distance)) / 2
    x2 = time - x1
    x1, x2 = sorted([x1, x2])
    x1, x2 = ceil(x1), ceil(x2)
    return x2 - x1


with open('input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
