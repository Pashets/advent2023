import math


def task_1(rows):
    instructions = rows[0].strip()
    len_instructions = len(instructions)
    network = dict()
    for row in rows[2:]:
        network[row[:3]] = (row[7:10], row[12:15])
    step = network['AAA']['LR'.index(instructions[0])]
    index_instruction = 1
    while step != 'ZZZ':
        step = network[step][
            'LR'.index(instructions[index_instruction % len_instructions])
        ]
        index_instruction += 1
    return index_instruction


def task_2(rows):
    instructions = rows[0].strip()
    len_instructions = len(instructions)
    network = dict()
    for row in rows[2:]:
        network[row[:3]] = (row[7:10], row[12:15])
    steps = [value['LR'.index(instructions[0])] for key, value in
             filter(lambda items: items[0][-1] == 'A', network.items())]
    destinations = set(filter(lambda key: key[-1] == 'Z', network))
    lens = []
    index_instruction = 1
    while len(lens) < 6:
        correct_steps = destinations& set(steps)
        if correct_steps:
            lens.extend([index_instruction] * len(correct_steps))
            destinations = destinations - set(steps)
        steps = [
            value[
                'LR'.index(instructions[index_instruction % len_instructions])
            ]
            for key, value in
            filter(lambda items: items[0] in steps, network.items())
        ]
        index_instruction += 1
    return math.lcm(*lens)


with open('input.txt') as f:
    lines = f.readlines()
    print(task_1(lines))
    print(task_2(lines))
