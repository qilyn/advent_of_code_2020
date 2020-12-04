from .utils import read_passports


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


def validate_passports():
    passports = read_passports()

    required = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        'cid',
    }

    valid = 0
    invalid = 0

    for passport in passports:
        passport['cid'] = True
        if set(passport.keys()) == required:
            valid += 1
        else:
            invalid += 1

    return valid, invalid
