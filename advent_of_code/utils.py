"""
Goal: count the number of passports that contain all fields except cid.

Valid fields:
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
"""

file = [l.strip() for l in open('../passport.txt').readlines()]


def read_passport(file):
    passports = []
    passport = {}

    num_passports = 0

    for line in file:
        if line == '':
            passports.append(passport)
            passport = {}
            num_passports += 1
            continue

        key_value = line.split(' ')

        for pair in key_value:
            key, value = pair.split(':')
            passport[key] = value

    passports.append(passport)
    num_passports += 1

    return passports


passports = read_passport(file)
