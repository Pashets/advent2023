from collections import Counter


def task_1(rows):
    bids_rows = []
    for row in rows:
        split_row = row.split()
        counter = Counter(split_row[0])
        bids_rows.append(
            (
                split_row[0],
                int(split_row[1]),
                list(filter(lambda key: key > 1,
                            sorted(counter.values(), reverse=True)))
            )
        )

    def _sort_by_values(values):
        if not values:
            return 0
        elif len(values) == 1:
            return values[0]
        else:
            return values[0] + 0.1 * values[1]

    def _sort_by_high_card(cards):
        base = 256
        sum_sort = 0
        for index, card in enumerate(cards, 1):
            if card.isdigit():
                ord_card = ord(card)
            else:
                ord_card = [*range(251, 256)]['TJQKA'.index(card)]
            sum_sort += base ** (len(cards) - index) * ord_card
        return sum_sort

    bids_rows = (
        sorted(
            bids_rows,
            key=lambda x: (_sort_by_values(x[2]), _sort_by_high_card(x[0])),
        )
    )
    return sum(
        index * points for index, (_, points, _) in enumerate(bids_rows, 1)
    )


def task_2(rows):
    bids_rows = []
    have_joker = False
    for row in rows:
        split_row = row.split()
        counter = Counter(split_row[0])
        if 'J' in counter and counter['J'] != 5:
            count_jokers = counter.pop('J')
            have_joker = True
        bids_rows.append(
            [
                split_row[0],
                int(split_row[1]),
                list(filter(lambda key: key > 1,
                            sorted(counter.values(), reverse=True)))
            ]
        )
        if have_joker:
            if bids_rows[-1][2]:
                bids_rows[-1][2][0] += count_jokers
            else:
                bids_rows[-1][2] = [count_jokers + 1]
        have_joker = False

    def _sort_by_values(values):
        if not values:
            return 0
        elif len(values) == 1:
            return values[0]
        else:
            return values[0] + 0.1 * values[1]

    def _sort_by_high_card(cards):
        base = 256
        sum_sort = 0
        for index, card in enumerate(cards, 1):
            if card.isdigit():
                ord_card = ord(card)
            else:
                ord_card = [251, 0, *range(253, 256)]['TJQKA'.index(card)]
            sum_sort += base ** (len(cards) - index) * ord_card
        return sum_sort

    bids_rows = (
        sorted(
            bids_rows,
            key=lambda x: (_sort_by_values(x[2]), _sort_by_high_card(x[0])),
        )
    )
    return sum(
        index * points for index, (_, points, _) in enumerate(bids_rows, 1)
    )


with open('input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
