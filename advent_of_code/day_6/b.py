"""
Goal: count the number of questions answered 'yes' by everyone in a group, for
each group.
"""


def count_all_group_answers():
    file = open('day_6/data/customs.txt').readlines()
    return count_file_answers(file)


def count_file_answers(file):
    """
    Given an iterable of lines, count the 'yes' answers given by everyone in a
    group.
    >>> count_file(['a', 'abc', 'abcd'])
    1
    """
    total = 0
    # Track the current group size and answers.
    group_size = 0
    group_answers = []

    for line in file:
        line = line.strip()

        # Every line represents a new member of the group.
        if line == '':
            # An empty line represents the end of our group!
            # Now we can sum the number of values that were present in every
            # line.
            total += count_group_answers(group_answers, group_size)
            group_size = 0
            group_answers = []
            continue

        group_size += 1

        for char in line:
            group_answers.append(char)

    # Include the last group of the file, which had no empty line after it.
    total += count_group_answers(group_answers, group_size)

    return total


def count_group_answers(group_answers, group_size):
    """
    Iterate through this group's answers and count the number of characters
    that equal group size.
    """
    group_count = 0
    for char in set(group_answers):
        if group_answers.count(char) == group_size:
            group_count += 1
    return group_count


print(count_yeses())
