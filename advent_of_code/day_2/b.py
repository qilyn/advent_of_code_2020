from .utils import split_rule_and_password

"""
Goal: find the number of valid passwords based on lines in an input file:

d-D w: X

where d and D are indices of two characters in string X
w is an alphabet character, and
X is some password

X must contain w at either d or D, but not both.
"""


def get_indices(indices):
    pos1, pos2 = indices.split('-')
    return (int(pos1) - 1, int(pos2) - 1)


def count_valid_passwords():
    inputs = open('data/passwords.txt').readlines()

    valid = 0
    invalid = 0

    for line in inputs:
        # Remove whitespace
        line = line.strip()

        rule, char, password = split_rule_and_password(line)
        first, second = get_indices(rule)

        # If only one of the characters at these two indices are a match:
        if ((password[first] == char) ^ (password[second] == char)):
            valid += 1
        else:
            invalid += 1

    return valid, invalid
