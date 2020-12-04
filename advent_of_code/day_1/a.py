"""
Goal: evaluate an expense report and find the two values that sum to 2020.
"""


def load():
    return sorted([
        int(i)
        for i in open('advent_of_code/day_1/data/input.txt').readlines()
    ])


def possibility_permutation():
    inputs = load()

    for i in range(len(inputs)):
        first = inputs[i]
        for j in range(i + 1, len(inputs) - 2):
            second = inputs[j]

            if first + second == 2020:
                return (first, second)
