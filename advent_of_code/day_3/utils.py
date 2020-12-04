INCREMENTS = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def toboggan(forest, by_x, by_y):
    trees = 0
    x = y = 0
    cell_width = len(forest[0])

    while y < len(forest):
        if forest[y][x % cell_width] == '#':
            trees += 1

        x += by_x
        y += by_y

    return trees
