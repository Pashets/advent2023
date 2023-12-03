from collections import defaultdict


class Dict(dict):
    def __setitem__(self, key, value):
        if self.get(key, 0) < value:
            return super().__setitem__(key, value)


def get_max_counts_for_games(rows: list[str]):
    max_counts_for_games = defaultdict(Dict)
    for index_row, row in enumerate(rows):
        row = row.rstrip()
        row = row[row.index(':') + 2:]
        sets = row.split('; ')
        for every_set in sets:
            for count_and_color in every_set.split(', '):
                count, color = count_and_color.split()
                max_counts_for_games[index_row + 1][color] = int(count)
    return max_counts_for_games


def task_1(rows: list[str]):
    max_counts_for_games = get_max_counts_for_games(rows)
    sum_correct = 0
    for index, counts_colors in max_counts_for_games.items():
        if counts_colors['red'] < 13 and counts_colors['green'] < 14 and \
                counts_colors['blue'] < 15:
            sum_correct += index
    return sum_correct


def task_2(rows: list[str]):
    max_counts_for_games = get_max_counts_for_games(rows)
    return sum(
        counts_colors['red'] * counts_colors['green'] * counts_colors['blue']
        for counts_colors in max_counts_for_games.values()
    )


with open('input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
