from .utils import split_rule_and_password


"""
Goal: find the number of valid passwords based on lines in an input file:

d-d: w X

where d-d is a range between two integers less than ten,
w is an alphabet character, and
X is some password

X must contain between d-d instances of w.
"""


def get_range(char_range):
    rule_min, rule_max = char_range.split('-')
    # Increment max by 1 as provided ranges are inclusive:
    return range(int(rule_min), int(rule_max) + 1)


def count_valid_passwords():
    """
    Return the number of valid and invalid passwords in the file.
    """
    inputs = open('data/passwords.txt').readlines()

    valid = 0
    invalid = 0

    for line in inputs:
        # Remove whitespace
        line = line.strip()

        char, char_range, password = split_rule_and_password(line)
        range_ = get_range(char_range)

        if password.count(char) in range_:
            valid += 1
        else:
            invalid += 1

    return valid, invalid


print(count_valid_passwords())
