"""
Goal: evaluate an expense report and find the three values that sum to 2020.
"""


def load():
    return sorted([
        int(i)
        for i in open('advent_of_code/day_1/data/input.txt').readlines()
    ])


def possibility_permutation():
    """
    I'm so excited to read other solutions to this problem. There's definitely
    something cool that I'm missing here.
    """
    inputs = load()
    possibilities = {}

    for i in range(len(inputs)):
        low = inputs[i]
        for j in range(i + 1, len(inputs) - 1):
            high = inputs[j]
            if low + high < 2020:
                possibilities[low + high] = (low, high)

    for total, values in possibilities.items():
        for i in inputs:
            if i in values:
                continue

            if total + i == 2020:
                return (i, values[0], values[1])
