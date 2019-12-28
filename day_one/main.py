import math

DAY_ONE_PART_ONE_INPUT = '../resources/day_one_part_one.txt'


def get_fuel_requirement(mass):
    answer = math.floor(mass / 3) - 2
    return 0 if answer <= 0 else answer


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
    total_for_all_masses = 0

    for mass in mass_list:
        total_fuel_for_mass = 0
        while mass > 0:
            current_fuel_requirement = get_fuel_requirement(mass)
            total_fuel_for_mass += current_fuel_requirement
            mass = current_fuel_requirement
        total_for_all_masses += total_fuel_for_mass
    return total_for_all_masses


print(F"day one, part one: {part_one()}")
print(F"day one, part two: {part_two()}")
