def load():
    return open('../passwords.txt').readlines()


def split_rule_and_password(line):
    """
    >>> split_rule_and_password(1-2 a: a)
    True
    >>> split_rule_and_password(1-2 a: aaa)
    True
    >>> split_rule_and_password(1-2 b: a)
    False
    """
    line = line.split(':')
    rule, char = line[0].split(' ')
    password = line[1].strip()
    return rule, char, password
