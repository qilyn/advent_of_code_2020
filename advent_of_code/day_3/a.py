from .utils import INCREMENTS, toboggan


def calculate_trees():
    inputs = [
        line.strip()
        for line in open('advent_of_code/day_3/data/map.txt').readlines()
    ]

    by_x, by_y = INCREMENTS[1:2]

    return toboggan(inputs, by_x, by_y)
