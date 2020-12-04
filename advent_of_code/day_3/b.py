from .utils import INCREMENTS, toboggan


def calculate_trees():
    inputs = [
        line.strip()
        for line in open('advent_of_code/day_3/data/map.txt').readlines()
    ]

    trees = []

    for by_x, by_y in INCREMENTS:
        trees.append(toboggan(inputs, by_x, by_y))

    total = 1

    for tree_count in trees:
        total = total * tree_count

    return total


print(calculate_trees())
