from typing import NamedTuple


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        x %= 141
        y //= 141
        self.x = x
        self.y = y


class Number:
    coord_start: Point
    coord_end: Point
    number: int
    used: bool = False

    def __init__(self, coord_start, coord_end, number):
        self.coord_start = coord_start
        self.coord_end = coord_end
        self.number = number

    def is_correct(self, symbol: "Symbol"):
        return (
                self.coord_start.x - 1 <= symbol.coord.x <= self.coord_end.x
                and
                self.coord_start.y - 1 <= symbol.coord.y <= self.coord_end.y + 1
        )


class SymbolTask1(NamedTuple):
    coord: Point


class SymbolTask2:
    coord: Point
    connected_points: list[Point]

    def __init__(self, coord: Point):
        self.coord = coord
        self.connected_points = []


def get_numbers_and_symbols_task_1(text):
    import re
    numbers = []
    symbols = []
    p = re.compile(r"\d+|[+@$/%#*\-=&]")
    for m in p.finditer(text):
        if m.group().isdigit():
            numbers += [Number(
                coord_start=Point(m.start(), m.start()),
                coord_end=Point(m.end(), m.end()),
                number=int(m.group())
            )]
        else:
            symbols += [SymbolTask1(
                coord=Point(m.start(), m.start()),
            )]
    return numbers, symbols


def get_numbers_and_symbols_task_2(text):
    import re
    numbers = []
    symbols = []
    p = re.compile(r"\d+|\*")
    for m in p.finditer(text):
        if m.group().isdigit():
            numbers += [Number(
                coord_start=Point(m.start(), m.start()),
                coord_end=Point(m.end(), m.end()),
                number=int(m.group())
            )]
        else:
            symbols += [SymbolTask2(
                coord=Point(m.start(), m.start()),
            )]
    return numbers, symbols


def task_1(rows):
    numbers, symbols = get_numbers_and_symbols_task_1(rows)
    correct_numbers = []
    for number in numbers:
        for symbol in symbols:
            if not number.used and number.is_correct(symbol):
                correct_numbers.append(number.number)
                number.used = True
    return sum(correct_numbers)


def task_2(rows):
    numbers, symbols = get_numbers_and_symbols_task_2(rows)
    for number in numbers:
        for symbol in symbols:
            if not number.used and number.is_correct(symbol):
                number.used = True
                symbol.connected_points.append(number)
    return sum(
        symbol.connected_points[0].number * symbol.connected_points[1].number
        for symbol in symbols
        if len(symbol.connected_points) == 2
    )


with open('input.txt') as f:
    text = f.read()
    print(task_1(text))
    print(task_2(text))
