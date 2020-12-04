def read_passports():
    file = [
        l.strip()
        for l in open('advent_of_code/day_4/data/passports.txt').readlines()
    ]

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
