def find_recursive_diffs(list_):
    diff = [list_[i] - list_[i - 1] for i in range(1, len(list_))]
    if any(diff):
        return [diff] + find_recursive_diffs(diff)
    return [diff]


def find_next_element(list_):
    diffs = find_recursive_diffs(list_)
    diff_last = 0
    for i in range(len(diffs) - 1, -1, -1):
        diff_last = diffs[i][-1] + diff_last
        diffs[i].append(diff_last)
    return list_[-1] + diff_last


def find_prev_element(list_):
    diffs = find_recursive_diffs(list_)
    diff_first = 0
    for i in range(len(diffs) - 1, -1, -1):
        diff_first = diffs[i][0] - diff_first
        diffs[i].insert(0, diff_first)
    return list_[0] - diff_first


def task_1(rows):
    return sum(find_next_element([*map(int, row.split())]) for row in rows)


def task_2(rows):
    return sum(find_prev_element([*map(int, row.split())]) for row in rows)


with open('input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
