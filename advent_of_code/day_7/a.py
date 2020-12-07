"""
mirrored silver bags contain 4 wavy gray bags.
clear tan bags contain 5 bright purple bags, 1 pale black bag, 5 muted lime bags.
dim crimson bags contain 5 vibrant salmon bags, 2 clear cyan bags, 2 striped lime bags, 5 vibrant violet bags.
"""

"""
How many bag colours can contain at least one shiny gold bag?
"""


def strip_colour(line):
    """
    >>> strip_colour('mirrored silver bags contain 4 wavy gray bags.')
    ('mirrored silver', ['wavy gray'])
    """
    # Remove whitespace and fullstop.
    subject, objects = line.strip()[:-1].split(' contain ')

    # Discard ' bag(s)
    subject = subject.split(' bag')[0]
    objects = [o.split(' bag') for o in objects]

    return subject, objects


def get_containers():
    file = open('data/input.txt').readlines()
