import math

DAY_ONE_PART_ONE_INPUT = '../resources/day_one_part_one.txt'


def get_fuel_requirement(mass):
    answer = math.floor(mass / 3) - 2
    return 0 if answer <= 0 else answer


def get_total_fuel_requirement(mass):
    if mass == 0:
        return mass
    current = get_fuel_requirement(mass)
    return current + get_total_fuel_requirement(current)


def file_to_list():
    mass_list = []
    with open(DAY_ONE_PART_ONE_INPUT) as fp:
        line = fp.readline()
        while line:
            mass = int(line.strip())
            mass_list.append(mass)
            line = fp.readline()
    return mass_list


def part_one():
    mass_list = file_to_list()
    return sum([get_fuel_requirement(mass) for mass in mass_list])


def part_two():
    mass_list = file_to_list()
    return sum([get_total_fuel_requirement(mass) for mass in mass_list])


print(F"day one, part one: {part_one()}")
print(F"day one, part two: {part_two()}")
