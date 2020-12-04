import re

from .utils import read_passports


"""
Goal: count the number of passports that meet the validation criteria.
"""


def _in_range(val, low, high):
    return val in range(low, high+1)


def birth_year(date):
    """
    Four digits; at least 1920 and at most 2002.
    """
    try:
        date = int(date)
    except TypeError:
        return
    else:
        return _in_range(date, 1920, 2002)


def issue_year(date):
    """
    Four digits; at least 2010 and at most 2020.
    """
    try:
        date = int(date)
    except TypeError:
        return
    else:
        return _in_range(date, 2010, 2020)


def expiry_year(date):
    """
    Expiration Year - four digits; at least 2020 and at most 2030.
    """
    try:
        date = int(date)
    except TypeError:
        return
    else:
        return _in_range(date, 2020, 2030)


def height(hgt):
    """
    Height - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    if hgt.endswith('cm'):
        try:
            hgt = int(hgt.strip('cm'))
        except TypeError:
            return
        else:
            return _in_range(hgt, 150, 193)
    elif hgt.endswith('in'):
        try:
            hgt = int(hgt.strip('in'))
        except TypeError:
            return
        else:
            return _in_range(hgt, 59, 76)


def hair(hcl):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    return bool(re.match(r'^#[0-9a-f]{6}$', hcl))


def eye_colour(ecl):
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def passport_id(pid):
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    return bool(re.match(r'\d{9}$', pid))


class PassportValidation:

    validator_map = {
        'byr': birth_year,
        'iyr': issue_year,
        'eyr': expiry_year,
        'hgt': height,
        'hcl': hair,
        'ecl': eye_colour,
        'pid': passport_id,
    }

    def validate(self):
        passports = read_passports()

        valid = []
        invalid = []

        for passport in passports:
            successes = set()

            for key, value in passport.items():
                if key == 'cid':
                    continue

                if self.validator_map[key](value):
                    successes.add(key)

            if successes == set(self.validator_map.keys()):
                valid.append(passport)
            else:
                invalid.append(passport)

        return len(valid), len(invalid)
