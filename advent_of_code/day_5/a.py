from collections import namedtuple


Seat = namedtuple('Seat', ['row', 'column', 'seat_id'])

"""
Goal: write a function to calculate the seat IDs.
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
"""


def slice_to_scale(low_, high_, char_, low_char='F'):
    """
    Given the current state of the low and high numbers, return the next range.
    """
    # print(low_, high_, end='')
    midpoint = round((high_ - low_) / 2 + low_)

    if char_ == low_char:
        value = [low_, midpoint]
    else:
        value = [midpoint, high_]

    # print(value)
    return value


def iterate(*, row, start, end, low_char):
    """
    Given a list to binary search, return the final value.
    """
    low = start
    high = end
    for char in row:
        # print(char, end='')
        low, high = slice_to_scale(low, high, char, low_char=low_char)

    if char == low_char:
        return low
    else:
        return high


def get_row_from_seat_partition(part):
    """
    >>> get_row_from_seat_partition('BFFFBBFRRR')
    (70, 7, 567)
    >>> get_row_from_seat_partition('FFFBBBFRRR')
    (14, 7, 119)
    >>> get_row_from_seat_partition('BBFFBBFRLL')
    (102, 4, 820)
    """
    row = part[0:7]
    col = part[7:]

    len_rows = 127
    len_cols = 7

    # print(row, col)

    row = iterate(row=row, start=0, end=len_rows, low_char='F')
    col = iterate(row=col, start=0, end=len_cols, low_char='L')

    return int(row), int(col), int((row*8) + col)


def get_highest_seat_id():

    file = open('./data/seats.txt').readlines()
    max_seat_id = 0

    for line in file:
        line = line.strip()
        _, _, seat_id = get_row_from_seat_partition(line)

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


print(get_highest_seat_id())