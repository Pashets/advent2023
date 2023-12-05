import re


def task_1(rows):
    s = 0
    for row in rows:
        numbers = re.findall(r'\d+', row)
        winning_numbers = {*map(int, numbers[1:11])}
        check_numbers = {*map(int, numbers[11:])}
        intersection = winning_numbers & check_numbers
        s += 2 ** (len(intersection) - 1) if intersection else 0
    return s


def task_2(rows):
    scratchcards_count_winning_numbers = []
    for row in rows:
        numbers = re.findall(r'\d+', row)
        winning_numbers = {*map(int, numbers[1:11])}
        check_numbers = {*map(int, numbers[11:])}
        intersection = winning_numbers & check_numbers
        scratchcards_count_winning_numbers.append(len(intersection))
    scratchcards_counts = [1] * len(rows)
    for i, count in enumerate(scratchcards_count_winning_numbers):
        for j in range(i + 1, i + 1 + count):
            scratchcards_counts[j] += scratchcards_counts[i]
    return sum(scratchcards_counts)


with open('input.txt') as f:
    text = f.readlines()
    print(task_1(text))
    print(task_2(text))
