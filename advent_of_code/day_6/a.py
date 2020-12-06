"""
Goal: count the number of questions answered 'yes' for each group.

The file is organised such that each group is empty newline separated, and
each member of that group is on its own line. A 'yes' answer simply means a
character is present.
"""


def count_yeses():
    file = open(
        '/home/vicki/workspace/advent_of_code_2020/advent_of_code/day_6/data/customs.txt'
    ).readlines()
    group_answers = [set()]

    for line in file:
        line = line.strip()

        if line == '':
            group_answers.append(set())

        for char in line:
            group_answers[i].add(char)

    total = 0

    for group_answer in group_answers:
        total += len(group_answer)

    print(group_answers)
    return total


print(count_yeses())
