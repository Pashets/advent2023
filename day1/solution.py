import re


def task_1(rows):
    s = 0
    for row in rows:
        q = re.findall(r'\d', row)
        s += int(q[0] + q[-1])
    return s


def task_2(rows):
    s = 0
    translates = {
        **{i: i for i in '123456789'},
        'ne': '1',
        'wo': '2',
        'hree': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'ight': '8',
        'ine': '9',
    }
    for row in rows:
        q = re.findall(
            r'\d|'
            r'(?<=o)ne|'
            r'(?<=t)wo|'
            r'(?<=t)hree|'
            r'four|'
            r'five|'
            r'six|'
            r'seven|'
            r'(?<=e)ight|'
            r'(?<=n)ine',
            row
        )
        s += int(translates[q[0]] + translates[q[-1]])
    return s


with open('day1/input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
